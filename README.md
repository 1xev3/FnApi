[![Discord](https://discordapp.com/api/guilds/564193469682155580/widget.png)](https://discord.gg/vgNpJbv)

# FnApi
This python api library for some information in fortnite.
This library contains: **Store, another store** (works without api key)**, items, item search, news, upcoming items**
***
## Getting Started
We need:
1. Register on the site: [link](https://fnapi.me/)
2. Create an API key on the same site
3. Download this package(pip install fnapi)
***
## Examples
#### shop.py
Displays today's items in the store
```python
from fnapi import Shop

token = 'HERE PASTE TOKEN' #register token at https://fnapi.me/
shop = Shop(token)
print(shop.date)

items = shop.get_items()
for item in items:
    print(item.id)          #get item id
    print(item.name)        #get item name
    print(item.price)       #get item price
    print(item.rarity)      #get item rarity
    print(item.type)        #get item type
    print(item.image)       #get link to item image
    print(item.icon)        #get link to item icon
    print(item.background)  #get link to item background
```
#### anotherShop
Displays today's items in the store.Does not require api key.It has several additional features.
```python
from fnapi import anotherShop
shop = anotherShop() #This shop does not require a token
print(shop.date)

items = shop.get_items()
for item in items:
    print(item.id)          #like example shopp
    print(item.name)        #...
    print(item.price)
    print(item.rarity)
    print(item.type)
    print(item.image)
    print(item.transparent)
    print(item.background)
    print(item.information)  #get item icon(with text/vbucks)
```
#### News
Displays news that appears when entering the battle royale.(and save the world)
```python
from fnapi import News

token = 'HERE PASTE TOKEN' #register token at https://fnapi.me/
newss = News(token)

all_news = newss.get_news()
for news in all_news:
    print(news.title) #news title
    print(news.image) #get link to image
    print(news.text)  #get news text
    print(news.adspace)#get adspace(up)
```
#### Items
Displays all items that are in the game (item store)
```python
from fnapi import Items

token = 'HERE PASTE TOKEN' #register token at https://fnapi.me/
it = Items(token)

#---find one item by name
it_f= it.find_item('Venus Flyer') #name
print(it_f.id)          #get id
print(it_f.name)        #get name
print(it_f.price)       #get price
print(it_f.rarity)      #get rarity
print(it_f.type)        #get item type(pickaxe/glider etc...)
print(it_f.image)       #get link to item image
print(it_f.background)  #get link to item icon

#---all items
items = it.get_items()
for item in items:     
   print(item.name)
   #...
```
#### Upcoming
Displays all items that have not yet appeared in the store.
```python
from fnapi import Upcoming

token = 'HERE PASTE TOKEN' #register token at https://fnapi.me/
it = Upcoming(token)

#---find one item by name
item_find= it.find_item('Fright Funk') #name
print(item_find.id)      #get id
print(item_find.name)    #get name
print(item_find.price)   #get price
print(item_find.rarity)  #get rarity
print(item_find.type)    #get item type(pickaxe/emote ... etc)
print(item_find.image)   #get item image (link to image)
print(item_find.background) #get item background(link to image)

#---all items 
items = it.get_items()
for item in items:     
   print(item.name)
   #...
```
