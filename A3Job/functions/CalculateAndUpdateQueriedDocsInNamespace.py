# This function calculates the total documents we have queried for a given namespace
# It will then update the JobInstanceNamespaceQueryCounts table with latest info
def lambda_handler(event, context):
    total_queried_docs_in_namespace = sum(event.get('query_namespace_in_parallel_output', []))

    namespace_summary = {
        'namespace': event.get('namespace'),
        'total_docs_in_namespace': event.get('namespace_info_and_query_batches').get('total_docs_in_namespace'),
        'total_queried_docs_in_namespace': total_queried_docs_in_namespace
    }

    # Save data into JobInstanceNamespaceQueryCounts table
    # Job Id, namespace, total_docs_count, total_docs_queried
    
    return namespace_summary

