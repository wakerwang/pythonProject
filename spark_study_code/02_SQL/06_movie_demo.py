# coding:utf8

from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.sql.types import StructType, StringType, LongType, IntegerType
import pandas as pd

from pyspark.sql import functions as F

if __name__ == '__main__':
    spark = SparkSession.builder.appName("test").master("local").getOrCreate()

    sc = spark.sparkContext

    schema = StructType(). \
        add("user_id", StringType(), nullable=True). \
        add("movie_id", StringType(), True).add("rank", IntegerType(), True). \
        add("ts", StringType(), True)

    df = spark.read.format("csv") \
        .option("sep", "\t") \
        .option("encoding", "utf-8") \
        .option("header", False) \
        .schema(schema=schema) \
        .load("../data/input/u.data")

    # TODO 用户平均分
    df.groupBy("user_id") \
        .avg("rank") \
        .withColumnRenamed("avg(rank)", "avg_rank") \
        .withColumn("avg_rank", F.round("avg_rank", 2)) \
        .orderBy("avg_rank", ascending=False) \
        .show()
    # TODO 电影的平均分查询

    df.createOrReplaceTempView("movie")

    spark.sql("""
        SELECT movie_id,ROUND(avg(rank),2) as avg_rank from movie group by movie_id order by avg_rank desc 
    """).show()

    # TODO 大于平均分的电影数量
    print("大于平均分的数量是：", df.where(df["rank"] > df.select(F.avg(df["rank"])).first()['avg(rank)']).count())

    # TODO   查询高分电影中打分次数最多的用户，此人打的平均分
    user_id = df.where("rank>3") \
        .groupBy("user_id") \
        .count() \
        .withColumnRenamed("count", "cnt") \
        .orderBy("cnt", ascending=False) \
        .limit(1).first()["user_id"]

    df.filter(df['user_id'] == user_id).select(F.round(F.avg("rank"), 2)).show()

    # TODO 查询每个用户的最低最高打分

    df.groupBy("user_id"). \
        agg(
        F.round(F.avg("rank"), 2).alias("avg_rank"),
        F.min("rank").alias("min_rank"),
        F.max("rank").alias("max_rank")
    ).show()

    # TODO 查询评分超多100次的电影的平均分排名top10

    df.groupBy("movie_id") \
        .agg(
        F.count("movie_id").alias("cnt"),
        F.round(F.avg("rank"), 2).alias("avg_rank")
    ).where("cnt>100")\
        .orderBy("avg_rank",ascending=False)\
        .limit(10)\
        .show()
