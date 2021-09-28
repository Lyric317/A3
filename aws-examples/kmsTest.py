import json
import boto3

def lambda_handler(event, context):
    
    # s3
    # get and delete
    # can get object only if lambda role is added to "key users"
    # can delete directly
    s3 = boto3.client('s3')
    
    bucket_name = "finance.reports.test"
    file_name = "testPutByLambda.txt"
    
    original = s3.get_object(Bucket=bucket_name, Key=file_name)
    print(original['Body'].read().decode('utf-8'))
    
    s3.delete_object(Bucket=bucket_name, Key=file_name)
    
    
    #put
    # string = "afdsfadfs13424"
    # encoded_string = string.encode("utf-8")

    # bucket_name = "finance.reports.test"
    # file_name = "testPutByLambda.txt"
    # s3_path = file_name

    # s3_resource = boto3.resource("s3")
    # if bucket is encrypted by key, no need for serversideencryption or ssekmskeyid
    # s3_resource.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
    # if no SSEKMSKeyId, encrypt by creating an aws managed keys by default
    # s3_resource.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string, ServerSideEncryption="aws:kms", SSEKMSKeyId="arn:aws:kms:us-east-2:066717673947:key/c9afd882-99a3-4ec3-9a93-f5fcad102d3a")
    
    # dynamodb
    # all actions need to add lambda role as a key user first
    # get
    
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('Pets')
    
    # response = table.get_item(
    #     Key = {
    #         'id': '000'
    #     }
    #     )
    
    # if 'Item' in response:
    #     return response['Item']
    # else:
    #     return {
    #         'statusCode': 404,
    #         'body': 'Not Found'
    #     }
    
    # delete
    #table.delete_item(Key={'id':'3423'})
    
    # put
    # response = table.put_item(
    # Item = {
    #     'id': 'adfqre',
    #     'name': 'kmstest'
    # }
    # )
    
    return {
        'statusCode': 200
    }
