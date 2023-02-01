# coding:utf8

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark import SparkContext

if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("RDD2DF").getOrCreate()
    sc = spark.sparkContext

    # Load a text file and convert each line to a Row.
    lines = sc.textFile("../data/input/people.txt")

    parts = lines.map(lambda x: x.split(","))
    people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

    # Infer the schema, and register the DataFrame as a table.
    schemaPeople = spark.createDataFrame(people)

    schemaPeople.createOrReplaceTempView("people")

    teenagers = spark.sql("select * from people")

    rdd = teenagers.rdd.map(lambda p: "name_" + p.name + "_" + "age_" + str(p.age)).collect()

    for v in rdd:
        print(v)
