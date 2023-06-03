
This project is to transfer data in staging bucket to developing bucket.

But the following is the ### phase one:  
  print the jobTest02.json to CloudWatchLog when this jobTest02.json is uploaded into AWS S3 jobbuck bucket.
  
    The jobTest02.json is as the following:
      
     [{"_id": {"$oid": "5bbfd5d9dc6546158c8e85c2"}, "title": "Marketing Specialist03", "level": "Mid-Level", "jobType": "Part-time", "publishedDate": {"$date": "2020-11-27T00:00:00Z"}, "deadline": {"$date": "2021-09-23T00:47:51.343Z"}, "effictivePeriod": 300, "jobRequiredDegree": "本科以上", "country": "", "city": ["Melbourne"], "categories_list": ["digital-marketing"]}]
     
     

Setup:

    Preruquisite:  setup IAM role with AWS S3 full access policy and AWS LambdabasicExecutionCloudWatchRole
    
    
    => Log in with IAM role, follow the steps below:
    
Step one: 
     . Setup Lambda named s3LambdaFunc02 with permission of AWS S3 ReadOnly access
     . Set runtimes as Python 3.8
     . Copy and paste AWS S3 upload trigger lambda.py to code area
     
     ![](images / Figure1.png)
     
     

