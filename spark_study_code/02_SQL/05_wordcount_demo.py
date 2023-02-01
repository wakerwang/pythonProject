# coding:utf8

from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.sql.types import StructType, StringType, LongType, IntegerType
import pandas as pd

from pyspark.sql import functions as F

if __name__ == '__main__':
    spark = SparkSession.builder.appName("test").master("local").getOrCreate()

    sc = spark.sparkContext
    # rdd = sc.textFile("../data/input/dream").flatMap(lambda x: x.split(" ")) \
    #     .map(lambda x: [x])
    # df = rdd.toDF(["word"])
    #
    # df.createOrReplaceTempView("words")
    # spark.sql("select word,count(1) as cnt from words group by word order by cnt desc ").show()

    df2 = spark.read.format("text").load("../data/input/dream")
    # df2.printSchema()
    df2.show()

    df2.withColumn("word", F.explode(F.split(df2.value, ' '))).distinct().show(truncate=False)
