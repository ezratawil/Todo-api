# Todo-api 
Todo api using AWS lambda function with DynamoDB backend. Developed in Python using Chalice microframework for creating and developing Lambda Function and REST API , and AWS SDK for python (boto3) for configuring AWS resources. Resource Configuration in the file generate_table.py, and API logic in the app.py file

References used:                                         
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html     
https://chalice.readthedocs.io/en/stable/
## Configure Resources:
```
>>>> py generate_table.py

```
## Deployment to the cloud
```
>>>> chalice deploy
Creating deployment package.
Updating policy for IAM role: TODO-dev
Creating lambda function: TODO-dev
Creating Rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:us-east-2:596157085528:function:TODO-dev
  - Rest API URL: https://4pt8htt4vf.execute-api.us-east-2.amazonaws.com/api/

```


## Check for records in db
#### URL: https://4pt8htt4vf.execute-api.us-east-2.amazonaws.com/api/todos

```
>>>> http https://4pt8htt4vf.execute-api.us-east-2.amazonaws.com/api/todos
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 2
Content-Type: application/json
Date: Sun, 06 Feb 2022 16:25:59 GMT
Via: 1.1 c11768c6b1b5ff333d5fbf47fdd112fe.cloudfront.net (CloudFront)
X-Amz-Cf-Id: LyakSqfmDxEac7H36VH-JGxt-_G7XGsJ4JwN5ONDGjXOVjjHKKwFYQ==
X-Amz-Cf-Pop: TLV50-C2
X-Amzn-Trace-Id: Root=1-61fff696-7c1ae0131d336461356d5c6c;Sampled=0
X-Cache: Miss from cloudfront
x-amz-apigw-id: NIN3eFmLCYcFQ0A=
x-amzn-RequestId: 9aba8079-c28b-4dae-922d-2e473a5aacf9

[]

```
### Returns empty list (we havent added records yet) 


## Add first todo item to our table 
#### URL: https://4pt8htt4vf.execute-api.us-east-2.amazonaws.com/api/add_record

```
>>>> echo {"description": "TODO #1"} | http POST https://4pt8htt4vf.execute-api.us-east-2.amazonaws.com/api/add_record
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 36
Content-Type: application/json
Date: Sun, 06 Feb 2022 16:32:46 GMT
Via: 1.1 56706a0e74c90535106878a6a2f1475c.cloudfront.net (CloudFront)
X-Amz-Cf-Id: hF_yTwnayv9j194EFllDIrtE4jofjAxKSiNMjEwr-HU4pbFLy7RRPw==
X-Amz-Cf-Pop: TLV50-C2
X-Amzn-Trace-Id: Root=1-61fff82d-41b9f05908aef61007e51003;Sampled=0
X-Cache: Miss from cloudfront
x-amz-apigw-id: NIO3LH7zCYcFpfQ=
x-amzn-RequestId: f8680fc0-227b-42fa-b2ab-430ec92fa284

15c6bb66-70de-4d2c-9c7b-6220292c1d19 # uuid of record #1
```
### adding 2 more records

```
>>>> echo {"description": "TODO #2"} | http POST https://4pt8htt4vf.execute-api.us-east-2.amazonaws.com/api/add_record
HTTP/1.1 200 OK
...
15c6bb66-70de-4d2c-9c7b-6220292c1d19 

>>>> echo {"description": "TODO #3"} | http POST https://4pt8htt4vf.execute-api.us-east-2.amazonaws.com/api/add_record
HTTP/1.1 200 OK

23530c85-1490-4b87-8dd8-432048eecfd4

```
## List all Todos          
#### URL: https://4pt8htt4vf.execute-api.us-east-2.amazonaws.com/api/todos
```
>>>> http https://4pt8htt4vf.execute-api.us-east-2.amazonaws.com/api/todos
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 301
Content-Type: application/json
Date: Sun, 06 Feb 2022 16:42:18 GMT
Via: 1.1 b00e5a80ecee340cd80eb4bbb362e66c.cloudfront.net (CloudFront)
X-Amz-Cf-Id: 04OFEee8TiKIUPw1mR_QIx_D_q2Ob8FPtTgP14XTyyqT6MGqLs0wEA==
X-Amz-Cf-Pop: TLV50-C2
X-Amzn-Trace-Id: Root=1-61fffa6a-04fe8340042fee383e76e648;Sampled=0
X-Cache: Miss from cloudfront
x-amz-apigw-id: NIQQtEggCYcF3lw=
x-amzn-RequestId: 8331ee75-6c15-4bb9-8227-4623a3861e04

[
    {
        "data": {},
        "description": "TODO #2",
        "id": "743cfc6b-24e7-44ad-bc37-c81d3acdb46e",
        "state": "unstarted"
    },
    {
        "data": {},
        "description": "TODO #3",
        "id": "23530c85-1490-4b87-8dd8-432048eecfd4",
        "state": "unstarted"
    },
    {
        "data": {},
        "description": "TODO #1",
        "id": "15c6bb66-70de-4d2c-9c7b-6220292c1d19",
        "state": "unstarted"
    }
]

```


