from flask import Flask, request, jsonify
import subprocess
import logging
from pyspark.sql import SparkSession
from pyspark import SparkConf

# Spark configuration
conf = SparkConf()
conf.set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.0")
conf.set(
    "spark.hadoop.fs.s3a.aws.credentials.provider",
    "com.amazonaws.auth.InstanceProfileCredentialsProvider",
)
spark = SparkSession.builder.config(conf=conf).getOrCreate()

# Server
app = Flask(__name__)

# Logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/process", methods=["POST"])
def process_file():
    data = request.json

    logger.info(f"Data: {data}")

    bucket_name = data["bucketName"]
    file_key = data["filePath"]
    file_path = f"s3a://{bucket_name}/{file_key}"

    logger.info(f"Recebida solicitação para processar arquivo {file_path}")

    df = spark.read.json(file_path)

    return jsonify({"message": "Processamento iniciado pelo Spark."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
