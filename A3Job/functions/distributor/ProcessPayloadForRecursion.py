"""
    This function split batches if required
"""

def lambda_handler(event, context):

    # Get delta docs to be run
    delta_docs_to_run = event.get('delta_docs_to_run')
    print("delta_docs_to_run {}".format(delta_docs_to_run))

    max_parallel_executions = event.get("max_parallel_executions")

    return_value = event

    # If the list includes more than the maximum number of max_parallel_executions, then split into batches.
    # Otherwise return the data as is.
    if len(delta_docs_to_run) > max_parallel_executions:
        delta_docs_batches = []
        current_batch = {"batch_id": 0, "delta_docs_to_run": []}
        added = 0
        for doc in delta_docs_to_run:
            current_batch['delta_docs_to_run'].append(doc)
            added = 0
            if len(current_batch['delta_docs_to_run']) >= max_parallel_executions:
                delta_docs_batches.append(current_batch)
                new_batch_id = current_batch['batch_id'] + 1
                current_batch = {"batch_id": new_batch_id, "delta_docs_to_run": []}
                added = 1
        if added == 0:
            delta_docs_batches.append(current_batch)

        del return_value['delta_docs_to_run']
        return_value["delta_docs_batches"] = delta_docs_batches


    return return_value
