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
    