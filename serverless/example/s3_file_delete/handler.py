import boto3

def delete(bucket, prefix, s3client, delete_extension):
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
          s3client.delete_object(Bucket=bucket, Key=filedir)
          print(filename + "を削除しました")
          
      if 'NextContinuationToken' in response:
        next_token = response['NextContinuationToken']
      else:
        break
    else:
      break
    
# prefix下にあるファイル、ディレクトリ全てまとめて削除
def delete_all(bucket, prefix, s3client):
  next_token = ''

  while True:
    if next_token == '':
      response = s3client.list_objects_v2(Bucket=bucket, Prefix=prefix, StartAfter=prefix)
    else:
      response = s3client.list_objects_v2(Bucket=bucket, Prefix=prefix, StartAfter=prefix, ContinuationToken=next_token)

    if 'Contents' in response:
      contents = response['Contents']
      
      for content in contents:
        filedir = content['Key']
        filename = filedir.replace(prefix, '')
        s3client.delete_object(Bucket=bucket, Key=filedir)
        print(filename + "を削除しました")
          
      if 'NextContinuationToken' in response:
        next_token = response['NextContinuationToken']
      else:
        break
    else:
      break
    
def shopping_all_cache(event, context):
	bucket = 's3-delete-file'
	prefix = 'example/dir/' #削除対象のファイルがあるディレクトリ
	s3client = boto3.client('s3')
	delete_extension = '.cache' #削除対象の拡張子

	delete(bucket, prefix_2, s3client, delete_extension)