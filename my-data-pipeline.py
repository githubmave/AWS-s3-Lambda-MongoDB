import json
import boto3
import csv
import uuid
from datetime import datetime
import os
from pytz import timezone
import process_data
# connect to s3 bucket
s3=boto3.resource('s3')
#the local file path in the local machine
local_file='/tmp/world_cup.csv'
# connect to dynamobd
dynamodb=boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMO_TABLE'])
tz_sydney = timezone(os.environ['TZ_LOCAL'])
# get time stamp to the upload files
date = datetime.now(tz_sydney).strftime("%Y-%m-%d")
def run(event,context):
    # display the data structure of objects in event
    print("Stared\t\t" + str(event))
    # retrieved uploaded objects passed by event
    records = event['Records']
    for record in records:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            process_data(bucket,key,local_file)
def process_data(bucket,key,file):
    s3get(bucket,key,file)
    with open(file,mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            row_json = json.dumps(row)
            print(row_json)
            id=str(uuid.uuid4())
            table.put_item(
                 Item={
                      
                      'id':id,
                      'date':date,
                      'content':row_json
                 }
            )

def s3get(bucket,key,file):
     s3.object(bucket,key).download_file(file)

 