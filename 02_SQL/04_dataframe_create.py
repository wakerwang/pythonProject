# coding:utf8

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, LongType, IntegerType
import pandas as pd

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("df create") \
        .master("local") \
        .getOrCreate()

    sc = spark.sparkContext

    # schema = StructType().add("data", StringType(), False)
    # df1 = spark.read.format("text") \
    #     .schema(schema=schema) \
    #     .load("../data/input/people.txt")
    # df1.show()
    #
    # df2 = spark.read.format("json") \
    #     .load("../data/input/people.json")
    # df2.show()
    #
    # df3 = spark.read.format("csv") \
    #     .option("seq", ";") \
    #     .option("header", True) \
    #     .option("encoding", "utf8") \
    #     .schema("name STRING,age INT,job STRING") \
    #     .load("../data/input/people.json")
    # df3.show()

    # df4 = spark.read.format("parquet").load("../data/input/users.parquet")
    # df4.show()

    df = spark.read.format("csv").schema("id INT,subject string,score INT").load("../data/input/stu_sco")

    id_col = df["id"]
    subject_col = df["subject"]
    df.select(["id", "subject"]).show()

    df.select("id", "subject").show()

    df.select(id_col, subject_col).show()

    df.filter("score<99").show()

    df.filter(df["score"] < 99).show()

    df.groupBy("subject").count().show()

    df.groupBy(df["subject"]).count().show()
