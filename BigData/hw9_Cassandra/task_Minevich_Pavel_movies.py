#Task 2 data processing
import sys
from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import split, substring, col, trim, regexp_replace, explode, collect_list
from pyspark.sql.types import IntegerType

sc = SparkContext('yarn', 'sssp')
spark = SparkSession(sc)

df = spark.read.format("csv").options(header=True, inferSchema=True) \
	.load("/data/movielens/movies.csv")
trim_title = trim(df.title)
df = df.withColumn('title', trim_title).withColumn('title', regexp_replace('title', '["\)]', ''))
df = df.filter(col('genres') != '(no genres listed)')
df = df.withColumn("genres",explode(split("genres","[|]")))
df = df.groupBy("movieId", "title").agg(collect_list("genres").alias("genres"))
year_sub = substring(df.title, -4, 4)
df = df.withColumn('year', year_sub.cast(IntegerType())).na.drop('any')
df = df.select('movieId', 'title', 'year', 'genres').withColumnRenamed('movieId', 'movieid')

df \
    .write \
    .format("org.apache.spark.sql.cassandra") \
    .options(table="movies", keyspace=sys.argv[1]).mode("append").save()
