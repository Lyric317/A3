def lambda_handler(event, context):
    if event['iteration_count'] == 1:
        namespaceList = ['mac', 'docman', 'pwm', 'cct']
    else:
        # Get all data from JobInstanceNamespaceQueryCounts
        # For every namepsace
            # calculate the percentage and add to array if total_docs_read / total_docs < 90%
        namespaceList = ['mac', 'docman']

    result = {**event, 'namespaceList': namespaceList}

    # return result

    return {
        'namespaceList': namespaceList
    }
