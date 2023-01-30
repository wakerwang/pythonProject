# coding:utf8

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import count
from pyspark.sql.functions import col, pandas_udf
import pandas as pd

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:mmcount <file>", file=sys.stderr)
        sys.exit(-1)

    spark = (SparkSession.builder.appName("pymmcount").getOrCreate())
    mnm_file = sys.argv[1]

    mnm_df = (spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(mnm_file))
    count_mnm_df = (
        mnm_df.select("State", "Color", "Count").groupby("State", "Color").agg(count("Count").alias("Total")).orderBy(
            "Total", ascending=False))
    count_mnm_df.show(n=60, truncate=False)

    print("Total Row=%d" % count_mnm_df.count())


    def cubed(a: pd.Series) -> pd.Series:
        return a * a * a
