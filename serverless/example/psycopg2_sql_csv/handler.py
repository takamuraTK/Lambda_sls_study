import psycopg2
import csv
import os
import boto3
import gzip

param = {
    'host': os.environ.get('PG_HOST'),
    'user': os.environ.get('PG_USER'),
    'password': os.environ.get('PG_PASS'),
    'database': os.environ.get('PG_DBNM'),
    'port': int(os.environ.get('PG_PORT'))
}

def hello(event, context):
  s3 = boto3.resource('s3')
  bucket = s3.Bucket(os.environ.get('S3_BUCKET_NAME'))
  tmp_gz_dir = '/tmp/test.csv.gz'
  s3_gz_dir = 'folder/test.tsv.gz'
  
  # get sql
  with psycopg2.connect(**param) as conn:
    with conn.cursor() as cur:
      cur.execute(open('sql/test.sql', 'r').read())
      # sqlファイルから呼び出す場合
      
      # write tsv
      with gzip.open(tmp_gz_dir, mode='wt') as f:
        writer = csv.writer(f, delimiter=',')
        for row in cur:
          print(row)
          writer.writerow(row)

      # upload
      bucket.upload_file(tmp_gz_dir, s3_gz_dir)

    conn.commit()
    