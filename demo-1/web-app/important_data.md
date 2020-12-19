############## Demo-1 ##############
On AWS--
step 1 : Iam role sns, s3
setp 2 : lambda function
step 4 : aws ses email verification
step 5 :  

On Local ----
Docker - 
* `docker build -t lambda-demo .`
* `docker-compose up`


#################### Demo-2 ###############

############ Lambda ####################
Function Names : HelloWorldFunction
testEvent Name : HelloWorldTestEvent

```
# import the JSON utility package since we will be working with a JSON object
import json
# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
	# extract values from the event object we got from the Lambda service
	name = event['firstName'] +' '+ event['lastName']
	# return a properly formatted JSON object
	return {
	'statusCode': 200,
	'body': json.dumps('Hello from Lambda, ' + name)
	}
```

############ Gateway API ###############
1. build Rest API
2. endpoint edge optimised
3. API Name    : HelloWorldAPI
4. Post method
5. Integration Type : Lambdafunction: HelloWorldFunction
6. enable cors and 
7. Deploy 
8. Invoke URL  : https://c4u66enmll.execute-api.us-east-1.amazonaws.com/dev
9. test : {
            "firstName":"Grace",
            "lastName":"Hopper"
          }

################ Dynamodb ####################
1. Table Name         : Hello_World_Database
2. DYNAMODB TABLE ARN : arn:aws:dynamodb:us-east-1:453677434195:table/Hello_World_Database



################### update lambda Iam Inline policy ####### 
1. Inline ploicy : Name - HelloWorldDynamoPolicy
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "VisualEditor0",
"Effect": "Allow",
"Action": [
"dynamodb:PutItem",
"dynamodb:DeleteItem",
"dynamodb:GetItem",
"dynamodb:Scan",
"dynamodb:Query",
"dynamodb:UpdateItem"
],
"Resource": "YOUR-TABLE-ARN"
}
]
}


