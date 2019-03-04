#!/bin/bash

hadoop fs -test -e /user/cloudera/outputChuck
if [ $? -ne 1 ]; then
    hadoop fs -rmr /user/cloudera/outputChuck
    echo 'deleted original folder *************'
fi

#hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/cloudera/inputChuck -output /user/cloudera/outputChuck
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/cloudera/inputAssignment2 -output /user/cloudera/outputChuck
echo 'mapreduce finished -------------------------------------------'

hadoop fs -getmerge /user/cloudera/outputChuck/* indexPlainText
echo 'output merged -------------------------------------------'

cat indexPlainText | python converter.py indexFromMapReduce