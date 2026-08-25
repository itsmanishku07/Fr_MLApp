"""Spark session utilities for MLApp."""
from pyspark.sql import SparkSession
 
 
def get_spark_session(app_name="MLApp"):
    spark = SparkSession.builder \
        .appName(app_name) \
<<<<<<< HEAD
        .config("spark.sql.shuffle.partitions", "200") \
        .config("spark.sql.adaptive.enabled", "true") \
=======
        .config("spark.sql.shuffle.partitions", "400") \
        .config("spark.default.parallelism", "400") \
>>>>>>> ecd9158 (By Me - feat: optimize spark partitions for large datasets)
        .getOrCreate()
    return spark
