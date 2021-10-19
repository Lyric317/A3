# This function initializes the namespace list we need for the A3 Job Execution
def lambda_handler(event, context):
    if event['job_iteration_count'] == 1:
        namespace_list = ['mac', 'docman', 'pwm', 'cct']
    else:
        # Get all data from JobInstanceNamespaceQueryCounts
        # For every namepsace
            # calculate the percentage and add to array if total_docs_read / total_docs < 90%
        namespace_list = ['mac', 'docman']

    return {
        'namespace_list': namespace_list
    }
