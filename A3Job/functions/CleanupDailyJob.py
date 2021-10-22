import boto3
import json

"""

    JobDailyDelta S3 Bucket would have:
        <Date - business_date input>/[]

    This function will clean up the delta agreements in S3 bucket JobDailyDelta under <Date>/
    (with key based on the business_date input)

    Do we want to keep the transformed-delta-data??

    S3 VPCE / KMS -> JobDailyDelta delete whole folder based on the business_date

"""

def lambda_handler(event, context):

    return {
        'key': 'value'
    }


