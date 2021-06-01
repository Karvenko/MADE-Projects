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
	IN_DIR="/data/ids"
else
	IN_DIR=$1
fi

if [ -z $2 ]
then
	OUT_DIR="/user/made21q1_minevich/hw01"
else
	OUT_DIR=$2
fi

hdfs dfs -rm -r $OUT_DIR

yarn jar $HADOOP_STREAMING_JAR \
	-mapper ./mapper.py \
	-reducer ./reducer.py \
	-numReduceTasks 2 \
	-input $IN_DIR \
	-output $OUT_DIR \
	-file ./mapper.py \
	-file ./reducer.py

hdfs dfs -cat $OUT_DIR/part-00000 2>/dev/null | head -50 > hw2_mr_data_ids.out 
cat hw2_mr_data_ids.out
