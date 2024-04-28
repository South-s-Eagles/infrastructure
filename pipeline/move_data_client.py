# Código inteiramente gerado pelo gpt, nem foi testado

import boto3
import json
from pymongo import MongoClient

# Configurações do AWS S3
AWS_REGION = "us-east-1"  # Substitua pela sua região
BUCKET_NAME = "seu-bucket-s3"  # Substitua pelo nome do seu bucket S3
PREFIX = "caminho/para/os/json/"  # Substitua pelo prefixo do seu diretório

# Configurações do MongoDB
MONGODB_CONNECTION_STRING = (
    "mongodb://localhost:27017/"  # Substitua pelo seu endereço do MongoDB
)
DATABASE_NAME = "nome-do-banco"  # Substitua pelo nome do seu banco de dados
COLLECTION_NAME = "nome-da-colecao"  # Substitua pelo nome da sua coleção


def download_json_from_s3(bucket_name, prefix):
    """
    Baixa arquivos JSON do Amazon S3.
    """
    s3 = boto3.client("s3", region_name=AWS_REGION)
    paginator = s3.get_paginator("list_objects_v2")
    response_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    for page in response_iterator:
        if "Contents" in page:
            for obj in page["Contents"]:
                key = obj["Key"]
                if key.endswith(".json"):
                    file_name = key.split("/")[-1]
                    s3.download_file(bucket_name, key, file_name)
                    yield file_name


def insert_json_to_mongodb(file_name):
    """
    Insere dados JSON em um banco de dados MongoDB.
    """
    client = MongoClient(MONGODB_CONNECTION_STRING)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    with open(file_name, "r") as file:
        data = json.load(file)
        collection.insert_many(data)


def main():
    # Baixa arquivos JSON do S3 e os insere no MongoDB
    for file_name in download_json_from_s3(BUCKET_NAME, PREFIX):
        insert_json_to_mongodb(file_name)
        print(f"Arquivo {file_name} inserido no MongoDB com sucesso.")

    print("Todos os arquivos foram processados e inseridos no MongoDB.")


if __name__ == "__main__":
    main()
