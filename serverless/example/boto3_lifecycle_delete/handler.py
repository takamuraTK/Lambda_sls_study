import boto3
import os


# Prefixに指定したファイルにあるオブジェクトを作成から1日後、クリーンアップする
client = boto3.client('s3')
response = client.put_bucket_lifecycle_configuration(
  Bucket=os.environ.get('S3_BUCKET_NAME'),
  LifecycleConfiguration={
    'Rules': [
      {
        'Expiration': {'Days': 1},
        'ID': 'ms_export_csv',
        'Filter': {
          'Prefix': 'folder/dir/',
        },
        'Status': 'Enabled',
      },
    ]
  }
)



# 他にもバージョニングされたオブジェクトを削除したりする方法もあるので、
# 特定の拡張子のオブジェクトを削除するときはそれを使うといいかも

# Ruleのハッシュを別で記述してそれを代入するやり方もあり

# 公式ドキュメント
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_lifecycle_configuration

# 実例
# https://github.com/spulec/moto/blob/master/tests/test_s3/test_s3_lifecycle.py
