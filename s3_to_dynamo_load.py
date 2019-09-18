import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('td_notes_test')

def lambda_handler(TestEvent, context):
    bucket_name = TestEvent['Records'][0]['s3']['bucket']['name']
    s3_file_name = TestEvent['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
    data = resp['Body'].read().decode('utf-8')
    employees = data.split("\n")
    for emp in employees:
        emp_val = emp.split(",")
        print(emp_val[0])
        print(emp_val[6])
        table.put_item(
        Item = {"user_id": emp_val[0],
            "timestamp": emp_val[1],
            "content": emp_val[2],
            "title": emp_val[3],
            "cat": emp_val[4],
            "note_id": emp_val[5],
            "username": emp_val[6]
            }
        )