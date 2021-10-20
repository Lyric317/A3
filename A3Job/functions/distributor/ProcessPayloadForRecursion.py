"""
    This function split batches if required

    "delta_docs_to_run": [
        {
          "delta_doc_number": 0,
          "lex_id": "69988902-c227-41a0-824c-7a3996d799a0"
        },
        {
          "delta_doc_number": 40,
          "lex_id": "0d2fcf11-c41a-4bf6-ac07-c6eb7d2994ef"
        },
    ]
"""

def lambda_handler(event, context):

    # Get delta docs to be run
    delta_docs_to_run = event.get('delta_docs_to_run')
    print("delta_docs_to_run {}".format(delta_docs_to_run))

    # hardcoding for now
    max_parallel_executions = 40 # event.get("max_parallel_executions")

    return_value = event

    # If the list includes more than the maximum number of max_parallel_executions, then split into batches.
    # Otherwise return the data as is.
    if len(delta_docs_to_run) > max_parallel_executions: # e.g 558 > 40
        delta_docs_batches = []
        current_batch = {"batch_id": 0, "delta_docs_to_run": []}
        added = 0
        for doc in delta_docs_to_run:
            current_batch['delta_docs_to_run'].append(doc)
            added = 0 # re-set for after the below if has run
            if len(current_batch['delta_docs_to_run']) >= max_parallel_executions:
                # if we have appended 40, then create a new batch and replace the current batch
                delta_docs_batches.append(current_batch)
                new_batch_id = current_batch['batch_id'] + 1
                current_batch = {"batch_id": new_batch_id, "delta_docs_to_run": []}
                added = 1
        if added == 0:
            delta_docs_batches.append(current_batch)

        del return_value['delta_docs_to_run']
        return_value["delta_docs_batches"] = delta_docs_batches


    return return_value
