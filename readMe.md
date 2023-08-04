
## Purpose:
##### When AWS S3 has new files, would trigger Lambda to read and copy it to another S3 bucket 

 
##### print the jobTest02.json to CloudWatchLog when this jobTest02.json is uploaded into AWS S3 jobbuck bucket.
  
    The jobTest02.json is as the following:
      
     [{"_id": {"$oid": "5bbfd5d9dc6546158c8e85c2"}, "title": "Marketing Specialist03", "level": "Mid-Level", "jobType": "Part-time", "publishedDate": {"$date": "2020-11-27T00:00:00Z"}, "deadline": {"$date": "2021-09-23T00:47:51.343Z"}, "effictivePeriod": 300, "jobRequiredDegree": "本科以上", "country": "", "city": ["Melbourne"], "categories_list": ["digital-marketing"]}]
     
     

## Setup:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  setup IAM role with AWS S3 full access policy and AWS LambdabasicExecutionCloudWatchRole
    
    
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Log in with IAM role
    
## Step one: 
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Setup Lambda named s3LambdaFunc02 with permission of AWS S3 ReadOnly access
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set runtimes as Python 3.8
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Copy and paste AWS S3 upload trigger lambda.py to code area
     

##### When S3 bucket has new files coming in, send event notification
![image](https://github.com/githubmave/PipeLine-AWS-s3-Upload-Trigger-Lambda/assets/8073738/58121413-29f7-44fe-a6d1-2f0054a4aea8)

##### send event to lambda function


![image](https://github.com/githubmave/PipeLine-AWS-s3-Upload-Trigger-Lambda/assets/8073738/eb2e5ee0-f542-47c6-b0d4-1bcccb791f86)


## Set up Lambda function and deploy it 
![image](https://github.com/githubmave/PipeLine-AWS-s3-Upload-Trigger-Lambda/assets/8073738/68fe3477-c3c2-4281-
9916-9619a122fce1)


## Go to S3 bucket 
![image](https://github.com/githubmave/PipeLine-AWS-s3-Upload-Trigger-Lambda/assets/8073738/37608376-e9f4-446b-b9ec-55922cc7a77a)




     
     

