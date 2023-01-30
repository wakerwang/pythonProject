# coding:utf8

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, LongType, IntegerType

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("df create") \
        .master("local") \
        .getOrCreate()

    sc = spark.sparkContext

    rdd = sc.textFile("../data/input/people.txt") \
        .map(lambda x: x.split(",")) \
        .map(lambda x: (x[0], int(x[1])))

    schema = StructType(). \
        add("name", StringType(), True). \
        add("age", IntegerType(), True)

    df = spark.createDataFrame(rdd, schema=schema)

    df.show()
