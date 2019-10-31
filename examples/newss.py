from fnapi import News

token = 'HERE PASTE TOKEN' #register token at https://fnapi.me/
newss = News(token)

newss.get_news()
for news in newss.get_news():
    print(news.title) #news title
    print(news.image) #get link to image
    print(news.text)  #get news text
    print(news.adspace)#get adspace(up)