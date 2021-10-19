# This function will calculate the total amount of docs we've gotten and figure out if we comply with 90% or need to re-start
# or finally exit the A1 Job in case the max attempts are completed

# Input:
# {
#   "job_iteration_count": 1,
#   "max_parallel_executions": 2,
#   "query_batch_size": 100,
#   "namespace_list_to_query": {
#     "namespaces": [
#       "mac",
#       "docman",
#       "pwm",
#       "cct"
#     ]
#   },
#   "namespaces_summary": [
#     {
#       "namespace": "mac",
#       "total_docs_in_namespace": 2100,
#       "total_queried_docs_in_namespace": 2100
#     },
#     {
#       "namespace": "docman",
#       "total_docs_in_namespace": 2100,
#       "total_queried_docs_in_namespace": 2100
#     },
#     {
#       "namespace": "pwm",
#       "total_docs_in_namespace": 2100,
#       "total_queried_docs_in_namespace": 2100
#     },
#     {
#       "namespace": "cct",
#       "total_docs_in_namespace": 2100,
#       "total_queried_docs_in_namespace": 2100
#     }
#   ]
# }
def lambda_handler(event, context):

#     event['job_iteration_count']
#     event.get('namespaces_summary').get('total_docs_in_namespace')
#     event.get('namespaces_summary').get('total_queried_docs_in_namespace')

#     for namespace in event.get('namespaces_summary')
#         sum(c.a for c in c_list)
#         total_docs_in_all_namespaces += namespace.get('total_docs_in_namespace')
#         total_queried_docs_in_all_namespaces += namespace.get('total_queried_docs_in_namespace')

    # Calculate the total docs available in namespace
    total_docs_in_all_namespaces = sum(namespace.get('total_docs_in_namespace') for namespace in event.get('namespaces_summary'))
    total_queried_docs_in_all_namespaces = sum(namespace.get('total_queried_docs_in_namespace') for namespace in event.get('namespaces_summary'))

    job_iteration_count = event['job_iteration_count']
    should_retry_job = False
    should_fail_job = False
    if total_queried_docs_in_all_namespaces / total_docs_in_all_namespaces < 0.9:
        job_iteration_count += 1
        if job_iteration_count >= 4:
            should_fail_job = True
        else:
            should_retry_job = True

    return {
        'job_iteration_count': job_iteration_count,
        'should_fail_job': should_fail_job,
        'should_retry_job': should_retry_job,
        'total_docs_in_all_namespaces': total_docs_in_all_namespaces,
        'total_queried_docs_in_all_namespaces': total_queried_docs_in_all_namespaces
   }