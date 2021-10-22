import uuid
import boto3
import json

"""
    This function will fetch S3 bucket to calculate the total delta docs we've found
    It will then proceed to create the batching strategy for Docs transformation
    It will save the batch strategy to S3 for future usage

    Input:
    {
      "s3_bucket_name": "jobdailybatchprocessing",
      "max_parallel_executions": 2,
      "execution_name": "6ebf18c2-28c4-975f-3590-d6022229e2ba",
      "business_date": "10/20/2021"
    }

    Generates:
    {
        "delta_doc_batches": [
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
        ],
        "batch_index": [0...39]
    }

    S3 VPCE / KMS -> JobDailyDelta -> Read? we need to read only the kays within the folder of the business_date
    S3 VPCE / KMS -> jobdailybatchprocessing -> Write putObject
"""

# Initialize the S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):

    # Get all Objects's hash lex id from S3 Bucket JobDailyDelta for the day...
        # <Date - business_date input>/[]
    # Get total delta agreements from the S3 Bucket JobDailyDelta based on the date for the folder name
    total_delta_agreements = 1115
    print("total delta agreements from the JobDailyDelta is {}".format(total_delta_agreements))

    # Build batching strategy
    batches = []
    for i in range(total_delta_agreements):
        # Determine the batch id for this doc by mod of event.get("max_parallel_executions")
        batch_id = i % event.get("max_parallel_executions", 40) # 0 to 39

        # Start an object for this batch
        batch = {}
        if batch_id < len(batches):
            # Then this batch exists already. Get the existing batch object
            batch = batches[batch_id]
        else:
            # Then this is a new batch. Initalize the batch object
            batch = {"batch_number": batch_id, "delta_docs_to_run": []}
            batches.append(batch)

        # Get the existing list of delta docs to run
        delta_docs_to_run_list = batch["delta_docs_to_run"]

        # Get the doc id from delta docs bucket
        lex_id = str(uuid.uuid4()) # Generate a guid for now

        # Build the delta doc object that needs to be transformed and add it to the delta_docs_to_run_list list
        delta_doc = {"delta_doc_number": i, "lex_id": lex_id}
        delta_docs_to_run_list.append(delta_doc)
        
        # Re-set the list for this batch
        batch["delta_docs_to_run"] = delta_docs_to_run_list

        # Re-set the batch on the collection of batches
        batches[batch_id] = batch

    # Create an index of batches
    batch_index = []
    for b in batches:
        batch_index.append(b['batch_number'])

    print("Writing results to S3")
    # Put the batch info to s3

    # Get the execution name
    s3_key = 'execution_input/{}.json'.format(event.get('execution_name'))
    s3_bucket = event.get('s3_bucket_name')

    return_object = {"delta_doc_batches": batches, "batch_index": batch_index, "s3_bucket": s3_bucket, "s3_key": s3_key}

    response = s3_client.put_object(
        Bucket=s3_bucket,
        Key=s3_key,
        Body=json.dumps(return_object)
    )

#     print("Clearing delta doc batches from return data")
#     del return_object["delta_doc_batches"]
#     del return_object["s3_bucket"]
#     del return_object["s3_key"]
#
#     return return_object

    return {
        "batch_index": batch_index
    }




