import requests
import time

class item_():
    def __init__(self, json):
        self.id = json['itemId']
        self.name = json['item']['name']
        self.price = json['store']['cost']
        self.rarity = json['item']['rarity']
        self.type = json['item']['type']
        self.image = json['item']['images']['featured']
        self.icon = json['item']['images']['icon']
        self.background = json['item']['images']['background']

class Shop():
    def __init__(self,token,lang = 'en'):
        try:
            shop = requests.get('https://fnapi.me/api/shop/?lang='+lang,headers = {'authorization':token}).json()
            self.items = shop['data']
        except Exception as e:
            print('Error: '+str(e)+'\nSite returned: '+str(shop))
        self.date = time.strftime('%d.%m.%Y')

    def get_items(self):
        items = []
        for i in self.items:
            item = item_(i)
            items.append(item)
        return items