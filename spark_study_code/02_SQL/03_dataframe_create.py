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

    pdf = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["王龙龙", "胖平", "萌姐"],
        "age": [18, 17, 19]
    })

    spark.createDataFrame(pdf).show()
