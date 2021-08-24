# Adapted from @JustinCallison
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import json
import time
import random
import os
import uuid 
import boto3

# Initialize the s3 client
s3_client = boto3.client('s3')


def lambda_handler(event, context):

    # Get the number of docs from previous state
    total_docs = event.get('total_docs')
    print("total number of docs is {}".format(total_docs))

    # Get the execution name, default to a guid if not provided
    execution_name = event.get('execution_name',uuid.uuid4())

    # Set the maximum number of batches
    max_batches = 40

    # # Get the name of the s3 bucket to put things in from an environment variable
    # s3_bucket = ''
    # for k in os.environ:
    #     if k.lower() == 's3bucket':
    #         s3_bucket = os.environ[k]
    
    # Hardcode s3_bucekt for now
    s3_bucket = 'intermediarys3buckettobuildbatches'
    
    
    # Build the result
    print("Building results for {} docs.".format(total_docs))
    batches = []
    for i in range(total_docs):
        # Determine the batch id for this iteration by mod of max_batches
        bid = i % max_batches

        # Start an object for this batch
        batch = {}
        if bid < len(batches):
            # Then this batch exists already. Get the existing batch object
            batch = batches[bid]
        else:
            # Then this is a new batch. Initalize the batch object
            batch = {"batch_number": bid,"trans_to_run": []}
            batches.append(batch)


        # Get the existing list of tests to run
        trans_list = batch["trans_to_run"]
        
        # Get the doc id from delta docs bucket
        # Generate a guid for now
        doc_id = str(uuid.uuid4())

        # Build the object to transforme late 
        trans = {"trans_number": i,"doc_id": doc_id}
        
        # Add it to the list
        trans_list.append(trans)

        # Re-set the list for this batch
        batch["trans_to_run"] = trans_list

        # Re-set the batch on the collection of batches
        batches[bid] = batch

    # Create an index of batches 
    batch_index = []
    for b in batches:
        batch_index.append(b['batch_number'])

    print("Writing results to S3")
    # Put the batch info to s3
    s3_key = 'execution_input/{}.json'.format(execution_name)
    return_object = {"trans_batches": batches,"batch_index": batch_index,"s3_bucket":s3_bucket,"s3_key": s3_key}
    response = s3_client.put_object(
        Bucket=s3_bucket,
        Key=s3_key,
        Body=json.dumps(return_object)
    )

    print("Clearing trans batches from return data")
    del return_object["trans_batches"]

    return return_object
