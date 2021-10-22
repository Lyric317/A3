"""
    This function will call LEX once per namespace and get the total number of docs in the namespace
    It will then build an array of batch_index of size depending on the total number of docs available e.g. 1% of the total docs unless it reaches
    the max_parallel_executions (40 is the max we can have)

    VPCE interface to Inet
"""

def lambda_handler(event, context):
    # Query LEX with current namespace and get the total number of docs in the namespace
    print(event.get('namespace').get('namespace'))
    total_docs = 2100

    # Minimize the parallel executions when we have a very small number of documents in the namespace
    # we can have a max concurrent execution based on the 1% of the total docs
    # Hardcoding this value for now
    namespace = event['namespace']
    namespace['total_docs'] = total_docs

    # Hardcoding this for now.. but will need to change based on rule we come up with
    max_parallel_query_executions = event.get('max_parallel_executions') if total_docs > 5000  else 2
    namespace['batch_index'] = [i for i in range(max_parallel_query_executions)]

    return {
        **event,
        'max_parallel_query_executions': max_parallel_query_executions
    }

    # return {
    #     **event,
    #     'max_parallel_query_executions': max_parallel_query_executions,
    #     'total_docs': total_docs,
    #     'batch_index': [i for i in range(max_parallel_query_executions)]
    # }


# # This function will call LEX once per namespace and get the total number of docs in the namespace
# # It will then build an array of batch_index on size dictated by max_parallel_executions input
# def lambda_handler(event, context):
#     # query LEX with current namespace and get the total_docs
#     total_docs = 2100

#     # Get the input object for the namespace
#     namespace = event.get('namespace')
#     # Set the total of docs for the namespace
#     namespace['total_docs'] = total_docs

#     print(namespace)

#     # batch_data_obj['delta_doc_batches'][batch_id]
#     # 'namespaces': [n['namespace'] for n in event.get('namespaces_metadata', []) if n['run']]

#     namespaces_metadata = [namespace if n.namespace == namespace.namespace else n for n in namespaces_metadata]

#     max_parallel_executions = event.get('max_parallel_executions') if total_docs > 5000  else 2
#     batch_index = [i for i in range(max_parallel_executions)]

#     result = {**event, 'namespaces_metadata': namespaces_metadata, 'batch_index': batch_index}
#     return {
#         'total_docs': total_docs,
#         'batch_index': batch_index
#     }