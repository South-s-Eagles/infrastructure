import os
import json
from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://<username>:<password>@tx-cluster.2p3coke.mongodb.net/aguias?retryWrites=true&w=majority&appName=tx-cluster")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    raise

def lambda_handler(event, context):
    try:
        print("Evento recebido: ", event)
        
        message = event["requestPayload"]["Records"][0]["Sns"]["Message"]

        message_str = json.loads(message)
        message_data = json.loads(message_str)
        print("Mensagem convertida: ", message_data)

        db = client.aguias
        collection = db.test

        result = collection.insert_one(message_data)

        if result.inserted_id:
            return {
                'statusCode': 201,
                'body': "Document inserted successfully"
            }
        else:
            return {
                'statusCode': 500,
                'body': "Failed to insert document"
            }

    except Exception as e:
        print(f"Erro durante a execução: {e}")
        return {
            'statusCode': 500,
            'body': f"Erro: {str(e)}"
        }
