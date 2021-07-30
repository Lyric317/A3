# Notes: 

1. Select Python 3.8 as the Runtime for every Lambda function created
2. Step Function Execution Input

        {
          "deal": {
            "id": "4",
            "name": "secure2021"
          }
        }
3. Create DDB table "test-lambda-insert"
       
       Primary partition Key: Id

4. Create S3 Bucket "test-lambda-with-s3"

       Region: US East (N. Virginia) us-east-1