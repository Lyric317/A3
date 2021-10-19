import boto3
import json

"""
    Before Updating this, do we want some check if we have good amount of delta for the day??

    JobDailyDelta S3 Bucket would have:
        <Date - business_date input>/raw-delta-data/[]
        <Date - business_date input>/transformed-delta-data/[]

    This function will read the final set of delta agreements in S3 bucket JobDailyDelta under <Date>/transformed-delta-data/
    (with key based on the business_date input) and use this information to update the AgreementHash table
"""

def lambda_handler(event, context):

    return {
        'key': 'value'
    }


