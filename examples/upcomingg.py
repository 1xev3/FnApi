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