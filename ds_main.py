import json
import requests

def load_data_rooms(route_rooms):
    data_request = requests.get(route_rooms)
    data_rooms = json.loads(data_request.content)
    rooms = data_rooms.get('body')
    print(type(rooms))
    owners = []
    for room in rooms:
        room.pop('secondary_images')
        room.pop('main_image')
        room.pop('__v')
        
    
    print(type(rooms))
    # print(rooms)
    print(type(rooms[1]))

if __name__ == "__main__":
    route_rooms = 'https://backend-roompali.vercel.app/api/rooms'
    load_data_rooms(route_rooms)