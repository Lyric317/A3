import json
import boto3

# Initialize the s3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):

    print("Writing results to S3")
    # Put the batch info to s3

    s3_key = 'execution_input/{}.json'.format(event["id"])

    s3_bucket = 'test-lambda-with-s3'

    return_object = {"id": event["id"], "name": event["name"], "s3_bucket": s3_bucket, "s3_key": s3_key}

    response = s3_client.put_object(
        Bucket=s3_bucket,
        Key=s3_key,
        Body=json.dumps(return_object)
    )

    return return_object