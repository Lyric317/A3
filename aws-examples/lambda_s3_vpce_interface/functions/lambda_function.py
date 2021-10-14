import json
import boto3

# Initialize the s3 client
# s3_client = boto3.client('s3')
#this is needed when dealing with interface endpoints!!!
# it needs inbound security group rule + endpoint_url
# https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html?fbclid=IwAR3XyaLHkDmWMi3w7ooD27k_FhSgurdkPyPg5vnwz0PgvXCz_2Hmfntg6ro
s3_client = boto3.client(
    service_name='s3',
    region_name='us-east-2',
    endpoint_url='https://bucket.vpce-0324b765a77a48b93-l4z2gvkq.s3.us-east-2.vpce.amazonaws.com'
)

def lambda_handler(event, context):

    print("Writing results to S3")
    # Put the batch info to s3

    s3_key = 'execution_input/{}.json'.format(event["id"])

    s3_bucket = 'test-lambda-with-s3-east2'

    return_object = {
        "id": event["id"],
        "name": event["name"],
        "s3_bucket": s3_bucket,
        "s3_key": s3_key,
        "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }

    response = s3_client.put_object(
        Bucket=s3_bucket,
        Key=s3_key,
        Body=json.dumps(return_object)
    )

    return return_object
