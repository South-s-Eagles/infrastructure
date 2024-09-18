import os
import json
from pymongo import MongoClient

# Conectar ao MongoDB fora do handler
client = MongoClient("mongodb://")


def lambda_handler(event, context):
    try:
        # Imprimir evento recebido para debugging
        print("Evento recebido: ", event)

        # Acessar mensagem do evento SNS

        message = event["requestPayload"]["Records"][0]["Sns"]["Message"]

        message_str = json.loads(message)
        message_data = json.loads(message_str)
        print("Mensagem convertida: ", message_data)

        # Conectar ao banco e coleção
        db = client.aguias
        collection = db.sensores

        # Inserir documento
        result = collection.insert_one(message_data)

        if result.inserted_id:
            return {"statusCode": 201, "body": "Document inserted successfully"}
        else:
            return {"statusCode": 500, "body": "Failed to insert document"}

    except Exception as e:
        print(f"Erro durante a execução: {e}")
        return {"statusCode": 500, "body": f"Erro: {str(e)}"}
