# This function will call LEX once per namespace and get the total number of docs in the namespace
# It will then build an array of batch_index on size dictated by max_parallel_executions input
def lambda_handler(event, context):
    # query LEX with current namespace and get the total_docs_in_namespace
    print(event.get('namespace'))
    total_docs_in_namespace = 2100

    batch_index = [i for i in range(event.get('max_parallel_executions'))]
    return {
        'total_docs_in_namespace': total_docs_in_namespace,
        'batch_index': batch_index
    }
