### Step Function Input

    {
        "max_parallel_executions": 2,
        "query_batch_size": 1000,
        "business_date": "10-20-2021",
        "query_percentage_success": 0.9,
        "docs_transformation_percentage_success": 0.9,
        "namespaces": [
            {
                "namespace": "mac",
                "total_docs": 0,
                "total_docs_queried": 0
            },
            {
                "namespace": "docman",
                "total_docs": 0,
                "total_docs_queried": 0    
            },
            {
                "namespace": "pwm",
                "total_docs": 0,
                "total_docs_queried": 0    
            },
            {
                "namespace": "cct",
                "total_docs": 0,
                "total_docs_queried": 0
            }
        ]
    }


#### Readings:

Avoid Duplicate SFN
https://medium.com/@shweta2202/step-functions-preventing-duplicate-executions-a4f5f2868381

https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html

#### SFN ddb / kms:

    Jobstats: PutItem / updateItem / KMS

#### Lambdas with ddb / s3 / inet/ kms:
GetTotalDocsInNamespaceAndCreateBatchesForLexQuery:

    VPCE interface to Inet

QueryNamespace:
    
    VPCE interface to Inet
    DDB VPCE / KMS -> Agreement Hash -> read query?
    S3 VPCE / KMS -> JobDailyDelta -> create folder based on business_date
    S3 VPCE / KMS -> JobDailyDelta -> write putObject

CalculateAndUpdateQueriedDocsInNamespace:

    DDB VPCE / KMS -> JobInstanceNamespaceQueryCounts -> putItem

CreateBatchesForDeltaDocs:

    S3 VPCE / KMS -> JobDailyDelta -> Read? we need to read only the kays within the folder of the business_date
    S3 VPCE / KMS -> jobdailybatchprocessing -> Write putObject

GetDeltaDocsBatchInfo:
    
    S3 VPCE / KMS -> jobdailybatchprocessing -> Read getObject

TransformDocumentData:

    S3 VPCE / KMS -> JobDailyDelta -> Read (getObject)
    DDB VPCE / KMS -> GoverningLaw ->Read (getItem)
    DDB VPCE / KMS -> Entity -> Read (getItem)
    DDB VPCE / KMS -> Entity -> write (putItem)
    S3 VPCE / KMS -> JobDailyA3Data -> write (putObject)

CalculateTotalTransformedDocs: 
    
    S3 VPCE / KMS -> JobDailyA3Data -> write (get all keys with valid = false)

UpdateAgreementHashes: 

    S3 VPCE / KMS -> JobDailyA3Data -> read (get all keys (lex id) + hashPickwickObject with valid = true)
    DDB VPCE / KMS -> Agreement Hash -> write putItem in a loop?

CleanupDailyJob:

    S3 VPCE / KMS -> JobDailyDelta delete whole folder based on the business_date

#### Other Lambdas:
ValidateNamespacesQueryingProcess

ProcessPayloadForRecursion

CreateJobDailyA3Data
