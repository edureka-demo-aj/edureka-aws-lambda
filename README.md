# edureka-aws-lambda

## `Demo-1` ##
* `go to demo-1 folder`
* Step 1: `lambda function code : demo-lambda-47082852-b97b-41fd-8af2-5a7a78e4394d.zip`
* Step 2: `go to web-app folder`
* step 3: `docker build -t lambda-demo .`
* step 4: `docker-compose up` it will start your docker web application
* step 5: `set AWS SES :  under Email Address : verify email address`
* step 6: `create aws bucket`
* step 7: `update aws bucket with your bucket in lambda function and go to web-app folder update app.py`
* step 8: `set aws lambda function` and edit and replace your verified email address , bucket name,  
* step 9: `update IAM Role with following policy : 1. ses full access 2. s3 full access` for lambda function

## `Demo-2` ##
