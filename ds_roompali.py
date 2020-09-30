import json
import requests

def load_data(route):
  resp = requests.get(route)
  db_info_complete = json.loads(resp.content)
  rooms = db_info_complete.get('body')
  
  owner = rooms.get('owner')
  owner.pop('user_picture')
  owner.pop('__v')
  print('This is the owner information: ', owner)

  rooms.pop('secondary_images')
  rooms.pop('main_image')
  rooms.pop('owner')
  rooms.pop('__v')
  # print(rooms)
  print(type(rooms))
  for key, value in rooms.items():
    print (key, value)
  
if __name__ == "__main__":
    ##route = 'data/room1.json'
    route = 'https://backend-roompali.vercel.app/api/rooms/5f7200f824471e4eacf20656'
    load_data(route)