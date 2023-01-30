# coding:utf8

from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("df create") \
        .master("local") \
        .getOrCreate()

    sc = spark.sparkContext

    rdd = sc.textFile("../data/input/people.txt") \
        .map(lambda x: x.split(",")) \
        .map(lambda x: (x[0], x[1]))

    rdd.repartition(2)
    # schema=Struct

    df = spark.createDataFrame(rdd, schema=['name', 'age'])

    df.printSchema()
    df.show()

    df.createOrReplaceTempView("people")

    spark.sql("select * from people").show()
