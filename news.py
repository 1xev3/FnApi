import requests

class News_():
    def __init__(self, json):
        self.title = json['title']
        self.image = json['image']
        self.text = json['body']
        self.adspace = json['adspace']

class News():
    def __init__(self,token,lang = 'ru'):
        try:
            news = requests.get(f'https://fnapi.me/api/news/?lang={lang}',headers = {'authorization':token}).json()
            self.data = news['data']
        except Exception as e:
            print('Error: '+str(e)+'\nSite returned: '+str(news))
            if str(news) == "{'error': 'The Authorization is invalid'}":
                raise Exception('Token is invalid')

    def get_news(self):
        news = []
        for i in self.data:
            new = News_(i)
            news.append(new)
        return news