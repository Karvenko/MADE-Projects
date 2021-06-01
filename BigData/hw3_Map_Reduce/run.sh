#!/bin/bash
set -x
if [ -f "/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar" ]
then
	HADOOP_STREAMING_JAR="/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar"
else
	HADOOP_STREAMING_JAR="/usr/local/hadoop-2.10.0/share/hadoop/tools/lib/hadoop-streaming.jar"
fi

if [ -z $1 ] 
then
	IN_DIR="/data/stackexchange_part/posts"
else
	IN_DIR=$1
fi

if [ -z $2 ]
then
	OUT_DIR="/user/made21q1_minevich/hw03"
else
	OUT_DIR=$2
fi

hdfs dfs -rm -r -skipTrash ${OUT_DIR}*

( yarn jar $HADOOP_STREAMING_JAR \
	-D mapreduce.job.name="Stackoverflow. Phase 1" \
	-files ./mapper_stage_1.py,./reducer_stage_1.py\
	-mapper ./mapper_stage_1.py \
	-combiner ./reducer_stage_1.py \
	-reducer ./reducer_stage_1.py \
	-numReduceTasks 2 \
	-input $IN_DIR \
	-output ${OUT_DIR}_tmp &&

yarn jar $HADOOP_STREAMING_JAR \
        -D mapreduce.job.name="Stackoverflow. Phase 2" \
	-D stream.num.map.output.key.fields=2 \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D mapreduce.partition.keycomparator.options="-k1,1n -k2,2nr" \
	-D mapreduce.partition.keypartitioner.options="-k1.4,1.4" \
	-files ./mapper_stage_2.py,./reducer_stage_2.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
        -mapper ./mapper_stage_2.py \
        -reducer ./reducer_stage_2.py \
        -numReduceTasks 1 \
        -input ${OUT_DIR}_tmp \
        -output ${OUT_DIR}
) || "Something went wrong!!!"

hdfs dfs -rm -r -skipTrash ${OUT_DIR}_tmp
hdfs dfs -cat $OUT_DIR/part-00000 > hw3_mr_advanced_output.out 
cat hw3_mr_advanced_output.out
