from fnapi import stats as F


api = 'HERE PASTE TOKEN FROM https://fortnitetracker.com/site-api'
platform = 'pc'
nickname = '1xev3'

F.api_key = api
player = F.Stats(platform,nickname)

print(player.stats.CURRENT_DUO_KD)