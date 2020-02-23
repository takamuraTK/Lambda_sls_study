import boto3

bucket = "s3-delete-file"
prefix = "test_folder/folder/"
s3client = boto3.client('s3')
delete_extension = ".cache"

def delete(event, context):
  response = s3client.list_objects_v2(Bucket=bucket, Prefix=prefix, StartAfter=prefix)

  if 'Contents' in response:
    contents = response['Contents']

    for content in contents:
      filedir = content['Key']
      filename = filedir.replace(prefix, '')
      if delete_extension in filename:
        print(filename + "を削除します")
        # s3client.delete_object(Bucket=bucket, Key=filedir)
      else:
        print(filename + "は削除しません")

