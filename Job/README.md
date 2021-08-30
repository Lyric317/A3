# IAM Role
Step function
  - Add the policy for lambda function as normal
  - For a state machine that calls StartExecution for a single nested workflow execution, use an IAM policy that limits permissions to that state machine. To use the [Run a Job](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync) pattern (those ending in .sync), additional permissions are needed as follow.
    
    ` 
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "states:StartExecution"
            ],
            "Resource": [
                "arn:aws:states:[[region]]:[[accountId]]:stateMachine:[[stateMachineName]]"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "states:DescribeExecution",
                "states:StopExecution"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "events:PutTargets",
                "events:PutRule",
                "events:DescribeRule"
            ],
            "Resource": [
               "arn:aws:events:[[region]]:[[accountId]]:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule"
            ]
        }
    ]
}
`

https://docs.aws.amazon.com/step-functions/latest/dg/service-integration-iam-templates.html

https://docs.aws.amazon.com/step-functions/latest/dg/stepfunctions-iam.html

Main state machine should have permission of distributor. Distributor should have permission of itself.
