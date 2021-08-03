# Pre-requisites: 

1. Select Python 3.8 as the Runtime for every Lambda function created
2. Create DDB table "http-crud-tutorial-items"

       Primary partition Key: Id
3. This project uses API Gateway to call the Lambda function respectively. You can follow the instructions to set up an HTTP API here:  

       https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html

4. Once the HTTP API is created, you can run the below commands:

         curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"id\": \"abcdef234\", \"price\": 12345, \"name\": \"myitem\"}" https://d346nnrbob.execute-api.us-east-1.amazonaws.com/items
         
         curl -v https://d346nnrbob.execute-api.us-east-1.amazonaws.com/items
         
         curl -v  https://d346nnrbob.execute-api.us-east-1.amazonaws.com/items/abcdef234
         
         curl -v -X "DELETE"  https://d346nnrbob.execute-api.us-east-1.amazonaws.com/items/abcdef234
         
         curl -v  https://d346nnrbob.execute-api.us-east-1.amazonaws.com/items