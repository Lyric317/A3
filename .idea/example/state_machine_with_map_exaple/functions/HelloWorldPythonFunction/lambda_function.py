import json

def lambda_handler(event, context):
    print(event)

    return 'Hello ' + event['who'] + '!!!!'