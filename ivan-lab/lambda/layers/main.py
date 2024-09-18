import os
from pymongo import MongoClient


client = MongoClient(host="mongodb+srv://tx-adm-cl:7BoVvnfOXTCmZ5l8@tx-cluster.2p3coke.mongodb.net/aguias?retryWrites=true&w=majority&appName=tx-cluster")


def lambda_handler(event, context):
    # Name of database
    db = client.test 

    # Name of collection
    collection = db.test 
    
    # Document to add inside
    message = event["requestPayload"]["Records"][0]["Sns"]["Message"]
    message_str = json.loads(message)
    message_data = json.loads(message_str)

    # Insert document
    result = collection.insert_one(message_data)


    if result.inserted_id:
        return "Document inserted successfully"
    else:
        return "Failed to insert document"