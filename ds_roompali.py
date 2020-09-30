import json
import requests

def load_data(route):
  # with open(route) as content:
  #   db_info = json.load(content)
  #   print (db_info)
  resp = requests.get(route)
  db_info_complete = json.loads(resp.content)
  # db_info = db_info_complete.get('body')
  print(db_info_complete)
  # for rooms in db_info:
  #   print(db_info)


if __name__ == "__main__":
    ##route = 'data/room1.json'
    route = 'https://backend-roompali.vercel.app/api/rooms/5f720ed0afa65800077554f6'
    load_data(route)