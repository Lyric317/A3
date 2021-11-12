import json
import boto3

def lambda_handler(event, context):

    logger.info('...logging info...')
    
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    
    bucket = s3_resource.Bucket('testselect')
    docs = bucket.objects.filter(Prefix='11-12-21/')
    for doc in docs:
        r = s3_client.select_object_content(
            Bucket='testselect',
            Key=doc.key,
            ExpressionType='SQL',
            Expression="select s.hashLexId, s.pickwickObjectHash from S3Object s where s.isValid=true",
            InputSerialization={'JSON': {"Type": "Lines"}},
            OutputSerialization={'JSON': {}}
        )
    
        for event in r['Payload']:
            if 'Records' in event:
                records = json.loads(event['Records']['Payload'].decode('utf-8'))
                print(records['hashLexId'])
                print(records['pickwickObjectHash'])
