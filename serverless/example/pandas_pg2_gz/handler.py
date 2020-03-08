import boto3
import psycopg2
import os
import pandas as pd
import datetime

param = {
    'host': os.environ.get('PG_HOST'),
    'user': os.environ.get('PG_USER'),
    'password': os.environ.get('PG_PASS'),
    'database': os.environ.get('PG_DBNM'),
    'port': int(os.environ.get('PG_PORT'))
}

s3 = boto3.resource('s3')
bucket = s3.Bucket(os.environ.get('S3_BUCKET_NAME'))

def execute_sql_to_gzip(tmp, s3, sql_file):
  with psycopg2.connect(**param) as conn:
    df = pd.read_sql(sql=open('sql/{}'.format(sql_file), 'rt').read(), con=conn)
    df.to_csv(tmp, compression='gzip', index=False)
    bucket.upload_file(tmp, s3)

def execute(event, context):
  tmp_csv_dir = '/tmp/test.csv.gz'
  s3_csv_dir = 'folder/test.csv.gz'
  execute_sql_to_gzip(tmp_csv_dir, s3_csv_dir, 'test.sql')
  