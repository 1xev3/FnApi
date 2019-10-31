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
