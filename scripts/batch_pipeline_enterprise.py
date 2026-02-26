# ==========================================================
# ENTERPRISE BATCH DATA PIPELINE
# With Clear Console Output for Classroom
# ==========================================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, sum as _sum, avg, desc
from pyspark.sql.types import *
import logging
import os
import time

# ==========================
# START TIMER
# ==========================
start_time = time.time()

print("==========================================================")
print("   ENTERPRISE BATCH PIPELINE STARTED")
print("==========================================================")

# ==========================
# SETUP LOGGING
# ==========================
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/batch_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started")

# ==========================
# INITIALIZE SPARK
# ==========================
spark = SparkSession.builder \
    .appName("EnterpriseBatchPipelineDemo") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("Spark Session Initialized")
print("Spark Version:", spark.version)
print("----------------------------------------------------------")

# ==========================
# DEFINE SCHEMA
# ==========================
schema = StructType([
    StructField("transaction_id", StringType(), False),
    StructField("customer_id", StringType(), False),
    StructField("product", StringType(), True),
    StructField("category", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("transaction_date", StringType(), True)
])

# ==========================
# LOAD RAW DATA
# ==========================
print("Loading raw dataset...")

df = spark.read \
    .schema(schema) \
    .option("header", True) \
    .csv("data/raw/ecommerce_raw.csv")

df.cache()

raw_count = df.count()
print(f"Total Raw Records       : {raw_count}")
print("----------------------------------------------------------")

# ==========================
# CLEANING PHASE
# ==========================
print("Cleaning data...")

df_clean = df.dropDuplicates()

df_clean = df_clean.dropna(
    subset=["transaction_id", "customer_id", "price", "quantity"]
)

df_clean = df_clean.filter(
    (col("price") > 0) & (col("quantity") > 0)
)

df_clean = df_clean.withColumn(
    "transaction_date",
    expr("try_to_date(transaction_date, 'yyyy-MM-dd')")
)

df_clean = df_clean.dropna(subset=["transaction_date"])

clean_count = df_clean.count()
print(f"Total Cleaned Records   : {clean_count}")
print(f"Data Removed            : {raw_count - clean_count}")
print("----------------------------------------------------------")

# ==========================
# TRANSFORMATION
# ==========================
print("Applying transformation...")

df_transformed = df_clean.withColumn(
    "total_amount",
    col("price") * col("quantity")
)

print("Transformation completed")
print("----------------------------------------------------------")

# ==========================
# AGGREGATION
# ==========================
print("Calculating business metrics...")

# Category Revenue
df_curated = df_transformed.groupBy("category") \
    .agg(_sum("total_amount").alias("total_revenue"))

# Top 5 Products
df_top_products = df_transformed.groupBy("product") \
    .agg(_sum("quantity").alias("total_quantity")) \
    .orderBy(desc("total_quantity")) \
    .limit(5)

# Average Transaction Value per Customer
df_avg_transaction = df_transformed.groupBy("customer_id") \
    .agg(avg("total_amount").alias("avg_transaction_value"))

print("Aggregation completed")
print("----------------------------------------------------------")

# ==========================
# DISPLAY RESULTS
# ==========================
print("Top 5 Products:")
df_top_products.show()

print("Category Revenue:")
df_curated.show()

print("----------------------------------------------------------")

# ==========================
# SAVE DATA
# ==========================
print("Saving Clean Layer (Parquet)...")
df_transformed.write.mode("overwrite") \
    .parquet("data/clean/parquet/")

print("Saving Curated Layer...")
df_curated.write.mode("overwrite") \
    .parquet("data/curated/category_revenue/")

df_top_products.write.mode("overwrite") \
    .parquet("data/curated/top_products/")

df_avg_transaction.write.mode("overwrite") \
    .parquet("data/curated/avg_transaction/")

print("Saving Partitioned Data...")
df_transformed.write.mode("overwrite") \
    .partitionBy("category") \
    .parquet("data/clean/partitioned_by_category/")

print("----------------------------------------------------------")
print("All data successfully saved.")
print("----------------------------------------------------------")

# ==========================
# STOP SPARK
# ==========================
spark.stop()

end_time = time.time()
execution_time = round(end_time - start_time, 2)

print("==========================================================")
print(" PIPELINE COMPLETED SUCCESSFULLY ")
print(f" Total Execution Time: {execution_time} seconds")
print("==========================================================")

logging.info("Pipeline completed successfully")