import json
import requests
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f"Objeto S3 Recebido para ETL")

    url = os.getenv("SPARK_ENDPOINT")

    if not url:
        logger.error("Endpoint Spark não foi definido")
        return {
            "statusCode": 500,
            "body": "Variável de ambiente SPARK_ENDPOINT não foi definida",
        }

    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    file_path = event["Records"][0]["s3"]["object"]["key"]

    payload = {"bucketName": bucket_name, "filePath": file_path}

    payload_json = json.dumps(payload)

    print(payload)

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=payload_json)

    logger.info(payload)

    return {"statusCode": response.status_code, "body": response.text}
