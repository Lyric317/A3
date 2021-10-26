import json
import boto3
from datetime import date

def lambda_handler(event, context):
    # TODO implement
    print("input from eventbridge:")
    print(event)
    
    sfn_client = boto3.client('stepfunctions')
    
    sfn_input = {
        'date': date.today().strftime("%m/%d/%y")
    }
    
    response = sfn_client.start_execution(
        stateMachineArn='arn:aws:states:us-east-2:066717673947:stateMachine:testEventBridgeTrigger',
        name='testEventBridgeTriggerLambdaInVPCTriggerSfn',
        input=json.dumps(sfn_input)
    )
    
    
    return {
        'statusCode': 200,
        'body': 'success'
    }
