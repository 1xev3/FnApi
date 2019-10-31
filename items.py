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


class Items():
    def __init__(self,token,lang = 'eu'):
        data = requests.get(f'https://fnapi.me/api/items/all?lang={lang}',headers = {'authorization':token}).json()
        self.items = data['data']
        self.token = token

    def get_items(self):
        items = []
        for i in self.items:
            item = item_(i)
            items.append(item)
        return items

    def find_item(self,name:str):
        items = Items(self.token).get_items()
        for item in items:
            if str(item.name) == name:
                return item