
"""
    This function will call S3 JobDailyA3Data for all docs that have valid = false
    and compare the total with the percentage for transformation failure input,
    if false docs number is more than the passed percentage we'll fail job / re-try transformation?

    S3 VPCE / KMS -> JobDailyA3Data -> write (get all keys with valid = false)

"""

def lambda_handler(event, context):

    return {
        'key': 'value'
    }


