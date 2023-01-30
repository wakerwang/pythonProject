# /bin/env python
# coding:utf8
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[*]").setAppName("WC")
    sc = SparkContext(conf=conf)

    line_rdd = sc.textFile("../data/input/word")
    words_rdd = line_rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))

    result_rdd = words_rdd.reduceByKey(lambda a, b: a + b)
    print(result_rdd.collect())
