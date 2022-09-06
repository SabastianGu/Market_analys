from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.master("local[1]").appName('Coin analysis') \
    .getOrCreate() \
    
    spark.conf.set("spark.sql.extension.arrow.pyspark.enabled")
    spark.sparkContext.setLogLevel("ERROR")
