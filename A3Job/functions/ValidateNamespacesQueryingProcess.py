"""
    This function will calculate the total amount of docs we've gotten and figure out if we comply with 90% or need to re-start
    or finally exit the Job in case the max attempts are completed

    If the total_docs_queried / total_docs < 90%,
    1. Iterate through all of the namespaces and understand which one doesnt comply with total_docs_queried / total_docs > 90%
    2. For those above that dont comply with the above, create a new array of namespaces that will be re-tried (wipe out the totals)
    3. On the first iteration we need to keep these values, for future calculation
        total_docs_in_all_namespaces
        total_of_90%_comply_namespaces
    4. In case we are in a re-try, we need to calculate the full total based on
        total_of_90%_comply_namespaces + new_queried_totals_of_latest_retried_namespaces / total_docs_in_all_namespaces > 90%
    5. If not, repeat process
    6. Set a iterator_count variable and make it accessible for next time...


    Input:
    {
      "max_parallel_executions": 2,
      "query_batch_size": 1000,
      "business_date": "10/20/2021",
      "query_percentage_success": 0.9,
      "namespaces": [
        {
          "namespace": "mac",
          "total_docs": 2100,
          "total_docs_queried": 2100
        },
        {
          "namespace": "docman",
          "total_docs": 2100,
          "total_docs_queried": 2100
        },
        {
          "namespace": "pwm",
          "total_docs": 2100,
          "total_docs_queried": 2100
        },
        {
          "namespace": "cct",
          "total_docs": 2100,
          "total_docs_queried": 2100
        }
      ]
    }
"""


def lambda_handler(event, context):
    # Calculate the total docs available in namespaces that were just queried
    total_docs_in_all_namespaces = sum(namespace.get('total_docs') for namespace in event.get('namespaces'))
    total_queried_docs_in_all_namespaces = sum(namespace.get('total_docs_queried') for namespace in event.get('namespaces'))

    should_retry_job = False
    should_fail_job = False

    namespaces_to_re_run = []
    job_iteration_count = event.get('job_iteration_count', 1)
    if (job_iteration_count == 1):
        if total_queried_docs_in_all_namespaces / total_docs_in_all_namespaces < event.get('query_percentage_success'): #> 0.9:
            # namespaces_to_re_run = [n for n in event.get('namespaces') if n['total_docs_queried'] / n['total_docs'] > 0.9]
            namespaces_to_re_run = [n for n in event.get('namespaces') if n['total_docs_queried'] / n['total_docs'] < event.get('query_percentage_success')]
            print(namespaces_to_re_run)

            # TODO: substract the total_docs_queried from total_queried_docs_in_all_namespaces
            # TODO: substract the total_docs from total_docs_in_all_namespaces
            for n in namespaces_to_re_run:
                n['total_docs_queried'] = 0
                n['total_docs'] = 0

            job_iteration_count += 1
            if job_iteration_count >= 4:
                should_fail_job = True
            else:
                should_retry_job = True
    else:
        total_event.get('total_docs_in_all_namespaces')
    return {
        'job_iteration_count': job_iteration_count,
        'should_fail_job': should_fail_job,
        'should_retry_job': should_retry_job,
        'total_docs_in_all_namespaces': total_docs_in_all_namespaces,
        'total_queried_docs_in_all_namespaces': total_queried_docs_in_all_namespaces,
        'namespaces': namespaces_to_re_run
   }


#     # is_enough = True
#     # should_retry = False
#
#     should_fail = False
#     should_retry = False
#
#     attempts = event.get('result').get('attempts') if 'result' in event.keys() else 0
#     total_list = event.get('total_list')
#     total_should_get = 0
#     total_get = 0
#
#     for dic in total_list:
#         total_should_get += dic.get('total')
#         total_get += dic.get('total_get')
#
#     if total_get/total_should_get < 0.9:
#         attempts += 1
#         if attempts >= 3:
#             should_fail = True
#         else:
#             should_retry = True
#
#     return {
#         'attempts': attempts,
#         'should_retry': should_retry,
#         'should_fail': should_fail,
#         'total_docs': total_get
#     }
