import json

#input:
# namespace
# batch_size
# dynamodb_name
# businese_date

def lambda_handler(event, context):
    
    result = event
    
    # query namespace once and get total num of docs
    total = 2100
    thread_number = 2
    batch_index = [i for i in range(thread_number)]
    
    result['total'] = total
    result['thread_number'] = thread_number
    result['batch_index'] = batch_index
    
    return result
