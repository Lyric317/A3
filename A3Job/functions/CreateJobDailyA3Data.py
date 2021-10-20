import boto3
import json

"""
    This function would create the final set of data that is going to be ingested to Data Lake

    1. Read from JobDailyDelta S3 Bucket <Date - business_date input>/transformed-delta-data/[]
    2. Create necessary format for data lake and save the results to JobDailyA3Data with a folder with the input business_date
    3. Return the size of the transformed data
"""

def lambda_handler(event, context):

    return {
        'total_documents_processed': 1000
    }


