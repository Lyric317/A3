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


    Input 1st time:
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

    Input from 2 re-try onwards:
    {
      "max_parallel_executions": 2,
      "query_batch_size": 1000,
      "business_date": "10/20/2021",
      "query_percentage_success": 0.9,
      "job_iteration_count": 2,
      "should_fail_job": false,
      "should_retry_job": true,
      "total_docs_in_all_namespaces": 4200,
      "total_queried_docs_in_all_namespaces": 4200,
      "namespaces": [
        {
          "namespace": "mac",
          "total_docs": 0,
          "total_docs_queried": 0
        },
        {
          "namespace": "docman",
          "total_docs": 0,
          "total_docs_queried": 0
        }
      ]
    }

    90% 7560
"""


def lambda_handler(event, context):
  # Calculate the total docs available in namespaces that were just queried and sum them with existing value if available
  total_docs_in_all_namespaces = event.get('total_docs_in_all_namespaces', 0) + sum(namespace.get('total_docs') for namespace in event.get('namespaces'))
  total_queried_docs_in_all_namespaces = event.get('total_queried_docs_in_all_namespaces', 0) + sum(namespace.get('total_docs_queried') for namespace in event.get('namespaces'))

  should_retry_job = False
  should_fail_job = False

  job_iteration_count = event.get('job_iteration_count', 1)
  namespaces_to_re_run = event.get('namespaces')

  if total_queried_docs_in_all_namespaces / total_docs_in_all_namespaces < event.get('query_percentage_success'): #> 0.9:
    job_iteration_count += 1
    if job_iteration_count >= 4:
      should_fail_job = True
    else:
      should_retry_job = True
      namespaces_to_re_run = [n for n in event.get('namespaces') if n['total_docs_queried'] / n['total_docs'] < event.get('query_percentage_success')]
      print(namespaces_to_re_run)

      for n in namespaces_to_re_run:
          total_docs_in_all_namespaces -= n['total_docs']
          total_queried_docs_in_all_namespaces -= n['total_docs_queried']
          n['total_docs_queried'] = 0
          n['total_docs'] = 0

  # Replace namespace node and enrich output
  return {
    **event,
    'job_iteration_count': job_iteration_count,
    'should_fail_job': should_fail_job,
    'should_retry_job': should_retry_job,
    'total_docs_in_all_namespaces': total_docs_in_all_namespaces,
    'total_queried_docs_in_all_namespaces': total_queried_docs_in_all_namespaces,
    'namespaces': namespaces_to_re_run
  }