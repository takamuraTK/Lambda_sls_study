import boto3

bucket = "s3-delete-file"
prefix = "test_folder/folder/" #削除対象のファイルがあるディレクトリ
s3client = boto3.client('s3')
delete_extension = ".cache" #削除対象の拡張子

def delete(event, context):
  next_token = ''

  while True: #breakになるまで処理が続く。
    if next_token == '': # オブジェクト件数が1000個以上あった場合を想定
      response = s3client.list_objects_v2(Bucket=bucket, Prefix=prefix, StartAfter=prefix)
    else:
      response = s3client.list_objects_v2(Bucket=bucket, Prefix=prefix, StartAfter=prefix, ContinuationToken=next_token)
    # StartAfterに指定したそのキーよりも後のオブジェクトを取得する

    if 'Contents' in response:
      contents = response['Contents']

    for content in contents:
      filedir = content['Key']
      filename = filedir.replace(prefix, '')
      if delete_extension in filename:
        print(filename + "を削除します")
        s3client.delete_object(Bucket=bucket, Key=filedir)
      else:
        print(filename + "は削除しません") #確認のためのメッセージ、elseごとなくていい

    if 'NextContinuationToken' in response: # responseにオブジェクト件数が1000個以上あるときに発行されるやつ
      next_token = response['NextContinuationToken']
    else:
      break
