import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

# Create a SparkContext
sc = SparkContext()

# Create a GlueContext and SparkSession
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Get the job parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'input_path', 'output_path'])

# Get the input and output paths from Glue job parameters
input_path = args['input_path']
output_path = args['output_path']

# Read the CSV files from the input path using Spark DataFrame API
input_data = spark.read.csv(input_path, header=True, inferSchema=True)

# Convert CSV to Parquet
input_data.write.parquet(output_path)

# Stop the SparkContext
sc.stop()