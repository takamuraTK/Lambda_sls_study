import boto3

bucket = "s3-delete"
prefix = "test_folder/folder/"

def delete(event, context):
