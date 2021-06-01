from pyspark.sql.functions import col
from pyspark import SparkContext
from pyspark.sql.session import SparkSession

sc = SparkContext('yarn', 'sssp')
spark = SparkSession(sc)

START_POINT = 12
END_POINT = 34

#TWITTER_FILE = '/data/twitter/twitter_sample_small.txt'
#TWITTER_FILE = '/data/twitter/twitter_sample.txt'
TWITTER_FILE = '/data/twitter/twitter.txt'

init_data = [{'user_left': START_POINT}]
rdd = sc.parallelize(init_data)
init_df = spark.read.json(rdd)
init_df.cache()

tw_df = spark.read.format('csv').option('delimiter', '\t').load(TWITTER_FILE) \
        .withColumnRenamed('_c0', 'user').withColumnRenamed('_c1', 'follower').cache()

is_found = False
left_df = init_df
condition = (col('user_left') == col('follower'))
counter = 0

while not is_found:
    counter += 1
    left_df = left_df.join(tw_df, condition, 'inner').select(col('user')) \
    .distinct().withColumnRenamed('user', 'user_left').cache()
    #print(counter)
    #left_df.show()
    if left_df.filter(col('user_left') == END_POINT).count() > 0:
        is_found = True

print(counter)
