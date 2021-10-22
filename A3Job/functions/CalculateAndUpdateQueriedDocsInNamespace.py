"""
    This function calculates the total documents we have queried for a given namespace.
    It will enrich the namespace input with the total_docs_queried
    It will then update the JobInstanceNamespaceQueryCounts table with latest info

    {
      "execution_id": "arn:aws:states:us-east-1:112757862110:execution:A3JobSFN:9f1889dc-0eda-01d7-941f-d87b8bc36299",
      "query_batch_size": 1000,
      "namespace": {
        "namespace": "cct",
        "total_docs": 2100,
        "total_docs_queried": 0,
        "batch_index": [
          0,
          1
        ]
      },
      "max_parallel_executions": 2,
      "business_date": "10/20/2021",
      "max_parallel_query_executions": 2,
      "total_queried_data_per_batch": [
        1100,
        1000
      ]
    }

    DDB VPCE / KMS -> JobInstanceNamespaceQueryCounts -> putItem
"""

def lambda_handler(event, context):

  namespace = event['namespace']
  namespace['total_docs_queried'] = sum(event.get('total_queried_data_per_batch', []))

  del namespace['batch_index']

  # Save data into JobInstanceNamespaceQueryCounts table
  # Job Id ("execution_id"), namespace, total_docs_count, total_docs_queried

  return namespace



# def lambda_handler(event, context):

#     result = event

#     current_namespace_metadata = event.get('namespace_metadata')
#     current_namespace_metadata['total_docs'] = event.get('namespace_summary').get('total_docs')
#     current_namespace_metadata['total_docs_queried'] = sum(event.get('total_queried_data_per_batch', []))
#     print(current_namespace_metadata)

#     # Use current_namespace_metadata object to update namespaces_metadata in place
#     for i, n in enumerate(event.get('namespaces_metadata')):
#         if n.get('namespace') == current_namespace_metadata.get('namespace'):
#           result.get('namespaces_metadata')[i] = current_namespace_metadata

#     # Save data into JobInstanceNamespaceQueryCounts table
#     # Job Id ("execution_id"), namespace, total_docs_count, total_docs_queried

#     return result