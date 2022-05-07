import boto3
import json

ec2 = boto3.client('ec2')
# hello world
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    return {"statusCode": 200, "body": json.dumps(response)}
