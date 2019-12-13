from fnapi import stats as F

api = 'HERE PASTE TOKEN FROM https://fortnitetracker.com/site-api'
platform = 'pc'
nickname = '1xev3'

player = F.Stats(platform,nickname,api_key=api)

print(player.stats.CURRENT_DUO_KD)