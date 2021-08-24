import json

# {
#   "namespaces": ["a","b"],
#   "batch_size": 500,
#   "attempts": 0,
#   "dynamodb_name": "xx",
#   "businese_date": "8/13/2021",
#   "total_list": [
#     {
#       "total": 2100,
#       "total_get": 2100
#     },
#     {
#       "total": 2100,
#       "total_get": 2100
#     }
#   ]
# }
def lambda_handler(event, context):
    
    is_enough = True
    should_retry = False

    attempts = event.get('result').get('attempts') if 'result' in event.keys() else 0
    total_list = event.get('total_list')
    total_should_get = 0
    total_get = 0
    
    for dic in total_list:
        total_should_get += dic.get('total')
        total_get += dic.get('total_get')
    
    if total_get/total_should_get < 0.9:
        is_enough = False
        should_retry = True
        attempts += 1
        if attempts >= 3:
            should_retry = False
        
    return {
        'attempts': attempts,
        'is_enough': is_enough,
        'should_retry': should_retry,
        'total_docs': total_get
    }
