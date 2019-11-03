import requests

class item_():
    def __init__(self, json):
        self.id = json['itemId']
        self.name = json['item']['name']
        self.description = json['item']['description']
        self.price = json['item']['cost']
        self.rarity = json['item']['rarity']
        self.type = json['item']['typeName']
        self.image = json['item']['images']['icon']
        self.background = json['item']['images']['background']


class Upcoming():
    def __init__(self,token,lang = 'eu'):
        try:
            data = requests.get(f'https://fnapi.me/api/items/upcoming?lang={lang}',headers = {'authorization':token}).json()
            self.items = data['data']
            self.token = token
        except Exception as e:
            print('Error: '+str(e)+'\nSite returned: '+str(data))
            if str(data) == "{'error': 'The Authorization is invalid'}":
                raise Exception('Token is invalid')

    def get_items(self):
        items = []
        for i in self.items:
            item = item_(i)
            items.append(item)
        return items

    def find_item(self,name:str):
        items = Upcoming(self.token).get_items()
        for item in items:
            if str(item.name) == name:
                return item