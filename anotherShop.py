import requests
import time

class item_():
    def __init__(self, json):
        self.id = json['itemId']
        self.items = json['item']
        self.name = json['item']['name']
        self.price = json['store']['cost']
        self.rarity = json['item']['rarity']
        self.type = json['item']['type']
        self.image = json['item']['images']['featured']
        self.transparent = json['item']['images']['icon']
        self.background = json['item']['images']['background']
        self.information = json['item']['images']['information']


class anotherShop():
    def __init__(self):
        try:
            shop = requests.get('https://fortnite-api.theapinetwork.com/store/get').json()
            self.items = shop['data']
            self.date = time.strftime('%d.%m.%Y')
        except Exception as e:
            print('Error: '+str(e)+'\nSite returned: '+str(data))

    def get_items(self):
        items = []
        for i in self.items:
            item = item_(i)
            items.append(item)
        return items