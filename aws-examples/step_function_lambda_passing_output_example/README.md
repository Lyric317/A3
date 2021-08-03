# Notes: 
This example illustrates a call center. It includes one main step function with multiple lambdas. 
The lambdas take the output of one function as the input to the next.

1. Select Node.js 14.x as the Runtime for every Lambda function created
2. Step Function Execution Input

        {
          "inputCaseID": "003"
        }
