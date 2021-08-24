import json

# a simple counter pretend to query and get docs
# thread_number: the number of threads run parallely to query one namespace
# thread_index: 
# batch_size: size for this query
# total: total number of docs in this namespace
#result:
# total_get: total num of docs get from this namespace
# index: start index for this query

def lambda_handler(event, context):
    
    thread_number = event.get('thread_number')
    thread_index = event.get('thread_index')
    batch_size = event.get('batch_size')
    total = event.get('total')
    
    # if query for the first time, no query, thus no index, set as thread_index*batch_size
    if 'result' not in event.keys():
        index = thread_index * batch_size
        total_get = 0
    else:
        index = event.get('result').get('index')
        total_get = event.get('result').get('total_get')
        
    print("query from " + str(index))
    
    # todo: query and save to s3
    
    # pretend to get all for each query
    if total - index < batch_size:
        total_get += (total - index)
    else:
        total_get += batch_size 
    
    # pretend to fail by not update total_get
        
    index += thread_number * batch_size
    
    return {
        'index': index,
        'total_get': total_get
    }
