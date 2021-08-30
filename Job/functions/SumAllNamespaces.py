import json

# {
#   "namespaces": [
#     "a",
#     "b"
#   ],
#   "batch_size": 500,
#   "dynamodb_name": "xx",
#   "businese_date": "8/13/2021",
#   "total_list": [
#     {
#       "total": 1000,
#       "total_get": 1000
#     },
#     {
#       "total": 1000,
#       "total_get": 1000
#     }
#   ],
#   "result": {
#     "should_fail": false,
#     "should_retry": true,
#     "total_docs": 1000,
#     "attempts": 2
#   }
# }
def lambda_handler(event, context):
    
    # is_enough = True
    # should_retry = False
    
    should_fail = False
    should_retry = False

    attempts = event.get('result').get('attempts') if 'result' in event.keys() else 0
    total_list = event.get('total_list')
    total_should_get = 0
    total_get = 0
    
    for dic in total_list:
        total_should_get += dic.get('total')
        total_get += dic.get('total_get')
    
    if total_get/total_should_get < 0.9:
        attempts += 1
        if attempts >= 3:
            should_fail = True
        else:
            should_retry = True
        
    return {
        'attempts': attempts,
        'should_retry': should_retry,
        'should_fail': should_fail,
        'total_docs': total_get
    }
