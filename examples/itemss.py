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
#items = it.get_items()
#for item in items:     
#   print(item.name)
    #...