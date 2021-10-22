import boto3
import json

"""
    Before Updating this, do we want some check if we have good amount of delta for the day??

    JobDailyDelta S3 Bucket would have:
        <Date - business_date input>/[]

    This function will read the final set of delta agreements in S3 bucket JobDailyA3Data data/
    (with key based on the business_date input) and use this information to update the AgreementHash table
    We'll only hash the data that has valid = true...

    S3 VPCE / KMS -> JobDailyA3Data -> read (get all keys (lex id) + hashPickwickObject with valid = true)
    DDB VPCE / KMS -> Agreement Hash -> write putItem in a loop?

"""

def lambda_handler(event, context):

    return {
        'key': 'value'
    }


