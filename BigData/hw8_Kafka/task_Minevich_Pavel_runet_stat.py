import argparse
from pyspark.sql.functions import split
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.session import SparkSession

sc = SparkContext('yarn', 'domain_stat')
spark = SparkSession(sc)

sqlContext = SQLContext(sc)
sqlContext.setConf("spark.sql.shuffle.partitions", "3")

parser = argparse.ArgumentParser()
parser.add_argument("--kafka-brokers", required=True)
parser.add_argument("--topic-name", required=True)
parser.add_argument("--starting-offsets", default='latest')
group = parser.add_mutually_exclusive_group()
group.add_argument("--processing-time", default='0 seconds')
group.add_argument("--once", action='store_true')
args = parser.parse_args()

if args.once:
    args.processing_time = None
else:
    args.once = None

# Streaming for Task 1
df = spark.readStream.format('kafka').option("kafka.bootstrap.servers", args.kafka_brokers) \
    .option("subscribe", args.topic_name) \
    .option('startingOffsets', args.starting_offsets) \
    .load()

data_df = df.selectExpr('cast(value as string)')

split_col = split(data_df.value, '\t')

sp_df = data_df.select(split_col.getItem(0).alias('ts'),
                       split_col.getItem(1).alias('uid'),
                       split_col.getItem(2).alias('url'),
                       split_col.getItem(3).alias('title'),
                       split_col.getItem(4).alias('ua'))
sp_df.createOrReplaceTempView('sp_v')
spark.sql('select uid,parse_url(url, "HOST") as domain from sp_v').createOrReplaceTempView('sp_v2')
out_df = spark.sql('select domain, count(*) as view, approx_count_distinct(uid) as unique \
                    from sp_v2 group by domain order by view desc limit 10')
query = out_df.writeStream \
        .outputMode('complete') \
        .format('console') \
        .option('truncate', 'false') \
        .trigger(once=args.once, processingTime=args.processing_time) \
        .start()
query.awaitTermination()
