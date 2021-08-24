import json
import time
import random
import os
import uuid 
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):

    # Get the test to be run
    trans_to_run = event.get('trans_to_run')
    print("Trans To Run is {}".format(trans_to_run))

    # Set the max per batch
    max_per_batch = 40

    return_value = event
    
    # If the list includes more than the maximum number of tests, then split into batches. Otherwise return the data as is.
    if len(trans_to_run) > max_per_batch:
        trans_batches = []
        current_batch = {"batch_id": 0,"trans_to_run": []}
        added = 0
        for t in trans_to_run:
            current_batch['trans_to_run'].append(t)
            added = 0
            if len(current_batch['trans_to_run']) >= max_per_batch:
                trans_batches.append(current_batch)
                new_batch_id = current_batch['batch_id'] + 1
                current_batch = {"batch_id": new_batch_id,"trans_to_run": []}
                added = 1
        if added == 0:
            trans_batches.append(current_batch)
            
        del return_value['trans_to_run']
        return_value["trans_batches"] = trans_batches            


    return return_value
