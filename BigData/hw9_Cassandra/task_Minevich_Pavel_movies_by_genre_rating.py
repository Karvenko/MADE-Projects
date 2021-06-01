#Task 5 data processing
import sys
from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import split, substring, col, trim, regexp_replace, explode
from pyspark.sql.types import IntegerType

sc = SparkContext('yarn', 'sssp')
spark = SparkSession(sc)

r_df = spark.read.format("csv").options(header=True, inferSchema=True).load("/data/movielens/ratings.csv")
r_df = r_df.select('movieId', 'userId', 'rating') \
    .withColumnRenamed('movieId', 'movieid') \
    .withColumnRenamed('userId', 'userid')
df = spark.read.format("csv").options(header=True, inferSchema=True).load("/data/movielens/movies.csv")
trim_title = trim(df.title)
df = df.withColumn('title', trim_title).withColumn('title', regexp_replace('title', '["\)]', ''))
df = df.filter(col('genres') != '(no genres listed)')
year_sub = substring(df.title, -4, 4)
df = df.withColumn('year', year_sub.cast(IntegerType())).na.drop('any')
df = df.withColumn("genres",explode(split("genres","[|]")))
# df = df.groupBy("movieId", "title").agg(collect_list("genres").alias("genres"))

df = df.select('movieId', 'title', 'year', 'genres') \
    .withColumnRenamed('movieId', 'movieid') \
    .withColumnRenamed('genres', 'genre')

join_df = df.join(r_df, 'movieid', 'inner').na.drop('any')
join_df \
    .write \
    .format("org.apache.spark.sql.cassandra") \
    .options(table="movies_by_genre_rating", keyspace=sys.argv[1]).mode("append").save()

