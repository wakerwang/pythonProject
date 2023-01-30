# coding:utf-8

from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("log count") \
        .master("local") \
        .getOrCreate()

    sc = spark.sparkContext

    rdd = sc.textFile("E:\PycharmProjects\pythonProject\data\input\log") \
        .map(lambda x: x.split("\t"))\
        .map(lambda x:(x[3],x[8],x[10]))

    df=spark.createDataFrame(rdd, schema=['dt','status', 'link'])
    df.show(truncate=False)
    df.createOrReplaceTempView("tb")
    spark.sql("select count(*) from tb where link like '%domain1.com%'").show(truncate=False)


    spark.sql("select split(dt,'/')[2] from tb").show(truncate=False)


    # rdd = sc.textFile("E:\PycharmProjects\pythonProject\data\input\log") \
    #     .map(lambda x: x.split("\t"))
    #
    # df = spark.createDataFrame(rdd)
    # df.show(truncate=False)
