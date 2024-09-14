import json
from validators import validate_sensor_data

def lambda_handler(event, context):
    
    message = event["Records"][0]["Sns"]["Message"]
    message_str = json.loads(message)
    message_data = json.loads(message_str)
    err = validate_sensor_data(message_data)
    if (len(err) != 0):
        return {
            'statusCode': 400,
            'body': json.dumps(err)
            
        }
    return {
        'statusCode': 200,
        'body': message_data
        
    }
