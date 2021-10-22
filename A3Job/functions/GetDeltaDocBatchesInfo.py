import boto3
import json

"""
    This function loads the delta_doc_batches data from S3, filters for the corresponding batch_id
    and returns the data for further parallel processing

    {
      "batch_number": 0,
      "delta_docs_to_run": [
        {
          "delta_doc_number": 0,
          "lex_id": "69988902-c227-41a0-824c-7a3996d799a0"
        },
        {
          "delta_doc_number": 40,
          "lex_id": "0d2fcf11-c41a-4bf6-ac07-c6eb7d2994ef"
        },
      ]
    }

    S3 VPCE / KMS -> jobdailybatchprocessing -> Read getObject
"""

# Initialize the s3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):

    # Get the batch id from the input
    batch_id = int(event.get('batch_id'))
    print("batch_id is {}".format(batch_id))

    s3_key = 'execution_input/{}.json'.format(event.get('execution_name'))
    print("s3_key is {}".format(s3_key))
    s3_bucket = "jobdailybatchprocessing"

    # Load the full data from S3
    response = s3_client.get_object(
        Bucket=s3_bucket,
        Key=s3_key
    )

    batch_data = response['Body'].read().decode('utf-8')

    # Look for the batch in question and return it
    batch_data_obj = json.loads(batch_data)
    delta_doc_batch = batch_data_obj['delta_doc_batches'][batch_id]

    return delta_doc_batch


