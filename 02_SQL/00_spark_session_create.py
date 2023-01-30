# coding:utf8

from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName("test").master("local").getOrCreate()

    sc=spark.sparkContext

    rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)


    def add(num):
        return num * 10


    print(rdd.map(add).collect())