# -*- coding: utf-8 -*-
import requests
import json

def request(event, context):
  r = requests.get('https://books.rakuten.co.jp/event/book/comic/calendar/2020/02/js/booklist.json')
  # requestsを用いてgetでapiからjsonを取得

  json_dict = json.loads(r.text)
  # レスポンス(r.text)を辞書型にする

  books = json_dict['list']

  for book in books:
    print(book[5])

  print('合計' + str(len(books)) + '冊')