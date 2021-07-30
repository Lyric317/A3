import json
import boto3 # Latest AWS SDK for python
# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("test-lambda-insert")

    #print(table.table_status)

    deal = event["deal"]

    table.put_item(Item = {"id": deal['id'], "name": deal['name']})

    return event["deal"]