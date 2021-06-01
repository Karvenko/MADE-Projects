import re
from pyspark import SparkContext

sc = SparkContext('yarn', 'bigram')

def bigram_search(text, start_word='narodnaya'):
    result = []
    words = re.findall(r"\w+", text)
    for i, word in enumerate(words[:-1]):
        if word == start_word:
            result.append(words[i] + '_' + words[i + 1])
    return result

wiki_rdd = sc.textFile("hdfs:///data/wiki/en_articles_part")
wiki_rdd = (
    wiki_rdd
    .map(lambda x: x.split('\t', 1))
    .map(lambda pair: pair[1].lower())
    .map(bigram_search)
    .filter(lambda x: len(x) > 0)
    .flatMap(lambda x: [(y, 1) for y in x])
    .reduceByKey(lambda x, y: x + y)
)

results = wiki_rdd.takeOrdered(50)
for r in results:
    print(f'{r[0]}\t{r[1]}')

sc.stop()
