"""Wiki collocation counter"""
import re
import numpy as np
from pyspark import SparkContext

sc = SparkContext('yarn', 'bigram')

stop_words_rdd = sc.textFile("hdfs:///data/stop_words/stop_words_en-xpo6.txt")
stop_words_broadcast = sc.broadcast(stop_words_rdd.collect())
stop_words_fast = set(stop_words_broadcast.value)

def get_bigrams(text, stop_words):
    result = []
    words = re.findall(r"\w+", text)
    words = [w for w in words if w not in stop_words]
    for i in range(len(words) - 1):
        result.append((words[i], words[i + 1]))
    return result, words

wiki_rdd = sc.textFile("hdfs:///data/wiki/en_articles_part")
wiki_rdd_dual = (
    wiki_rdd
    .map(lambda x: x.split('\t', 1))
    .map(lambda pair: pair[1].lower())
    .map(lambda x: get_bigrams(x, stop_words_fast))
    .cache()
)

wiki_rdd_filtered = (
    wiki_rdd_dual
    .map(lambda x: x[0])
    .flatMap(lambda x: [(y, 1) for y in x])
    .reduceByKey(lambda x, y: x + y)
    .filter(lambda x: x[1] >= 500)
    .cache()
)

wiki_single_rdd = (
    wiki_rdd_dual
    .map(lambda x: x[1])
    .flatMap(lambda x: [(y, 1) for y in x])
    .reduceByKey(lambda x, y: x + y)
    .cache()
)

total_words = wiki_single_rdd.map(lambda x: x[1]).sum()

counted_stats = (wiki_rdd_filtered.map(lambda x: (x[0][0], (x[0][1], x[1])))
                 .join(wiki_single_rdd)
                 .map(lambda x: (x[1][0][0], (x[0], x[1][0][1], x[1][1])))
                 .join(wiki_single_rdd)
                 .map(lambda x: (x[1][0][0], x[0], x[1][0][1], x[1][0][2], x[1][1])).cache())

def count_npmi(ab_count, a_count, b_count, word_count=total_words):
    """Count npmi"""
    p_ab = ab_count / (word_count - 4100)
    p_a = a_count / word_count
    p_b = b_count / word_count
    return -np.log(p_ab / (p_a * p_b)) / np.log(p_ab)

final_result = (counted_stats
                .map(lambda x: (x[0], x[1], count_npmi(x[2], x[3], x[4])))
                .takeOrdered(39, key=lambda x: -x[2])
                )
for r in final_result:
    print(f'{r[0]}_{r[1]}\t{round(r[2], 3)}')

sc.stop()
