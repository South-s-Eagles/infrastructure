from flask import Flask, request, jsonify
import subprocess
import logging
from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

DESTINY_BUCKET_KEY = "client-souths-eagle-ivan/simulador"

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

    try:
        df_formatado.write.json(f's3a://{DESTINY_BUCKET_KEY}/{file_key}')
    except Exception as ex:
        logger.error(f"Não foi possível colocar o arquivo {file_key} no bucket {DESTINY_BUCKET_KEY}", ex)

    return jsonify({"message": "Processamento realizado pelo Spark."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


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