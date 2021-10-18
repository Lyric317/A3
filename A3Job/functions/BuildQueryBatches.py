def lambda_handler(event, context):
    # query namespace once and get total nums of docs

    total = 2100
    max_concurrency = 2
    batch_index = [i for i in range(max_concurrency)]

    return {
        'total': total,
        'max_concurrency': max_concurrency,
        'batch_index': batch_index
    }