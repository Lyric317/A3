import json

# input
# {
#   "batch_size": 500,
#   "namespace": "a",
#   "businese_date": "8/13/2021",
#   "dynamodb_name": "xx",
#   "total": 2100,
#   "thread_number": 2,
#   "batch_index": [0,1],
#   "result": [1100,1000]
# }
def lambda_handler(event, context):
    
    total_get = sum(event.get('result', []))
    
    return {
        'total': event.get('total'),
        'total_get': total_get
    }
