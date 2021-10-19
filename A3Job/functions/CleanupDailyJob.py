import boto3
import json

"""

    JobDailyDelta S3 Bucket would have:
        <Date - business_date input>/raw-delta-data/[]
        <Date - business_date input>/transformed-delta-data/[]

    This function will clean up the delta agreements in S3 bucket JobDailyDelta under <Date>/raw-delta-data/
    (with key based on the business_date input)

    Do we want to keep the transformed-delta-data??
"""

def lambda_handler(event, context):

    return {
        'key': 'value'
    }


