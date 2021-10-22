
"""
    In this function we'll transform all the docs in JobDailyDelta <Date - business_date input>/[] and save it into
    JobDailyA3Data

    All transformation logic:
    HERE
    Create child agreements

    We'll access:
    Governing Law table
    EMMA Entity table

    We'll do a schema validation and the transformation will be based on the namespace we are on...
        We'll start validating the counterparties and entities for the schema validation
        We'll start with valid = true for all documents
    If the validation is not correct, we'll add a valid = false attribute to the object and save it into JobDailyA3Data

    If entity is not available, we'll save it into the EmmaEntity table with id "x", we then put a message in a queue to
    enrich that entity.. a lambda will be call on the sqs message and it will invoke entity service to get the latest data
    and update the entity table

    S3 VPCE / KMS -> JobDailyDelta -> Read (getObject)
    DDB VPCE / KMS -> GoverningLaw ->Read (getItem)
    DDB VPCE / KMS -> Entity -> Read (getItem)
    DDB VPCE / KMS -> Entity -> write (putItem)
    S3 VPCE / KMS -> JobDailyA3Data -> write (putObject)
"""

def lambda_handler(event, context):

    return {
        'key': 'value'
    }


