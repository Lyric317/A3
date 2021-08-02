# Pre-requisites: 

1. We need to create 2 roles in IAM and attach them to every Step Functions and Lambdas we create.

    #### a. State Machine Role: "step_functions_basic_execution":
      Ensure you select "State Function" as the target AWS service
   
    ##### Attach Policies:
   
       CloudWatchLogsFullAccess
       AWSXrayFullAccess
       AWSLambdaRole
       AmazonSNSFullAccess

   #### b. Lambda Role: "lambda_basic_execution":
   Ensure you select "Lambda" as the target AWS service

   ##### Attach Policies:

       CloudWatchLogsFullAccess
       AWSXrayFullAccess
       AmazonS3FullAccess
       AmazonDynamoDBFullAccess
       AmazonSNSFullAccess
