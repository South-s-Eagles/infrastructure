from flask import Flask, request, jsonify
import boto3
import logging
import json
from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

DESTINY_BUCKET = "client-souths-eagle-ivan"

# S3 Configuration
s3 = boto3.client('s3')

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

# TODO: Tirar esse negócio estranho daqui depois
def categorizar_frequencia(hz):
    if 4 <= hz < 8:
        return "teta"
    elif 8 <= hz < 12:
        return "alpha"
    elif 12 <= hz < 30:
        return "beta"
    elif 30 <= hz < 40:
        return "gamma"
    else:
        return "outro"

def transform_data_frame_into_json(df):
    json_rdd = df.toJSON()
    json_list = json_rdd.collect()
    json_objects = [json.loads(json_str) for json_str in json_list]
    return json.dumps(json_objects, indent=2)

@app.route("/process", methods=["POST"])
def process_file():

    logger.info(f"Request to process ETL")

    data = request.json

    bucket_name = data["bucketName"]
    file_key = data["filePath"]
    file_path = f"s3a://{bucket_name}/{file_key}"

    logger.info(f"Recebida solicitação para processar arquivo {file_path} para o Bucket")

    df = spark.read.json(file_path)
    df_selecionado = df.select("dispositivoId", "dispositivo", "valor")
    categorizar_frequencia_udf = udf(categorizar_frequencia, StringType())
    df_formatado = df_selecionado.withColumn("tipo_frequencia", categorizar_frequencia_udf(df_selecionado.valor))
    json_data = transform_data_frame_into_json(df_formatado)

    s3.put_object(
            Bucket=DESTINY_BUCKET,
            Key=file_key,
            Body=(bytes(json_data.encode('UTF-8')))
    )

    logger.info("Dado tratado enviado para o S3")

    return jsonify({"message": "Processamento realizado pelo Spark."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

