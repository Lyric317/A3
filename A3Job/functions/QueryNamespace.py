# Query namespace
# total_docs_in_namespace: total num of docs in namespace
# max_parallel_executions
# batch_index
# batch_size: size for this query

# namespace_query_output:
    # query_from_index: start index for this query
    # total_docs_queried: so far for the namespace

def lambda_handler(event, context):
    batch_index = event['batch_index'] # event.get('batch_index')
    batch_size = event['batch_size'] # event.get('batch_size')
    # Set initial values when initially querying the namespace
    if 'namespace_query_output' not in event.keys():
        query_from_index = batch_index * batch_size # e.g. one thread (0*500) 0 | second thread (1*500) 500 | third thread (2*500) 1000
        total_docs_queried = 0
    else:
        query_from_index = event.get('namespace_query_output').get('query_from_index')
        total_docs_queried = event.get('namespace_query_output').get('total_docs_queried')


    # TODO
        # 1. Query QFC LEX Service based on the query_from_index
        # 2. Scan DDB Agreement Hash table and compare hashes with queried data
        # 3. Filter new / changed hashes
        # 4. Save to S3 JobDailyDelta

    # Pretend to query docs in namespace
    if event.get('total_docs_in_namespace') - query_from_index < event.get('batch_size'):
        total_docs_queried += (event.get('total_docs_in_namespace') - query_from_index)
    else:
        total_docs_queried += event.get('batch_size')

    query_from_index += event.get('max_parallel_executions') * event.get('batch_size')

    return {
        'query_from_index': query_from_index,
        'total_docs_queried': total_docs_queried
    }
