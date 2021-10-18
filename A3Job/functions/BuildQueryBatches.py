def lambda_handler(event, context):
    # query namespace once and get total nums of docs

    print(event.get('namespace'))

    total_docs_in_namespace = 2100
    max_parallel_executions = 2
    batch_index = [i for i in range(max_parallel_executions)]

    return {
        'total_docs_in_namespace': total_docs_in_namespace,
        'max_parallel_executions': max_parallel_executions,
        'batch_index': batch_index
    }
