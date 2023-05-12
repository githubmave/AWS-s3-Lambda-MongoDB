import json
import boto3
import csv
import uuid
from datetime import datetime
import process_data

s3=boto3.resource('s3')
local_file = '/tmp/world_cup.csv'
dynamobd =boto3.resource('dynamodb')
table = dynamobd.Table('demo_table')
date =datetime.now().strftime("%Y-%m-%d")
# retrieved data from s3 bucket 
def lambda_handler(event,context):
    #TODO implement
    records=event['Records']
    for record in records:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        process_data(bucket,key,local_file) 
def process_data(bucket,key,file):
    s3get(bucket,key,file)
    with open(file,mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            row_json=json.dumps(row)
            print(row_json)
            id=str(uuid.uuid4())
            table.put_item(
                Item={
                    'id': id,
                    'date': date,
                    'content': row_json
                }
            )
def s3get(bucket,key,file):
    s3.Object(bucket,key).download_file(file)