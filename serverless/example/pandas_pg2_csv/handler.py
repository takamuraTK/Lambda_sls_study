import psycopg2
import boto3
import os
import datetime
import pandas as pd

param = {
    'host': os.environ.get('PG_HOST'),
    'user': os.environ.get('PG_USER'),
    'password': os.environ.get('PG_PASS'),
    'database': os.environ.get('PG_DBNM'),
    'port': int(os.environ.get('PG_PORT'))
}

s3 = boto3.resource('s3')
bucket = s3.Bucket(os.environ.get('S3_BUCKET_NAME'))

def execute(event, context):
  tmp_csv_dir = '/tmp/test.csv'
  s3_csv_dir = 'folder/test.csv'
  
  with psycopg2.connect(**param) as conn: # DBへの接続の確立
    df = pd.read_sql(sql=open('sql/ms.sql', 'rt').read(), con=conn) # 接続にconnを用いてSQLファイルを実行し、結果をDataFrame型に代入する
    # ここで引数を指定する場合はparams={'hoge': hoge}とする
    
    df.to_csv(tmp_csv_dir, index=False) # indexは行数を表示するかどうか。デフォはTrueになっている
    bucket.upload_file(tmp_csv_dir, s3_csv_dir)
