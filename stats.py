import requests
from enum import Enum

api_key = None

class FortnitePlaylist(Enum):
    SOLO = "p2"
    DUO = "p10"
    SQUAD = "p9"
    CURRENT_SOLO = "curr_p2"
    CURRENT_DUO = "curr_p10"
    CURRENT_SQUAD = "curr_p9"

class Stats:

    def __init__(self, platform, user , api_key= None):
        if api_key == None:
            raise TypeError('Api key is required! Register at: https://fortnitetracker.com/site-api')
        self.api_key = api_key
        self.user = user
        self.platform = platform
        self.url = ""
        self.update_url()
        self.stats = None
        if self.api_key is not None:
            self.make_request()

    def set_user(self, user):
        self.user = user
        self.update_url()

    def set_platform(self, platform):
        self.platform = platform
        self.update_url()

    def update_url(self):
        self.url = f"https://api.fortnitetracker.com/v1/profile/{self.platform}/{self.user}/"
        if self.api_key is not None:
            self.make_request()

    def make_request(self):
        header = {"TRN-Api-Key": self.api_key}
        req = requests.get(self.url, headers=header)
        req.json()
        req.close()
        self.stats = FortniteStats.get_stats(req.json())
    
class FortniteStats:
    def get_stats(json):
        return FortniteStats(json)

    def __init__(self, json=None):
        if json is not None:
            self.json_data = json
            self.CURRENT_SOLO_SCORE = self.get_score(FortnitePlaylist.CURRENT_SOLO)
            self.CURRENT_DUO_SCORE = self.get_score(FortnitePlaylist.CURRENT_DUO)
            self.CURRENT_SQUAD_SCORE = self.get_score(FortnitePlaylist.CURRENT_SQUAD)
            self.CURRENT_SOLO_WINS = self.get_top_one(FortnitePlaylist.CURRENT_SOLO)
            self.CURRENT_DUO_WINS = self.get_top_one(FortnitePlaylist.CURRENT_DUO)
            self.CURRENT_SQUAD_WINS = self.get_top_one(FortnitePlaylist.CURRENT_SQUAD)
            self.CURRENT_SOLO_TOP_TWELVE = self.get_top_twelve(FortnitePlaylist.CURRENT_SOLO)
            self.CURRENT_DUO_TOP_TWELVE = self.get_top_twelve(FortnitePlaylist.CURRENT_DUO)
            self.CURRENT_SQUAD_TOP_TWELVE = self.get_top_twelve(FortnitePlaylist.CURRENT_SQUAD)
            self.CURRENT_SOLO_TOP_TWENTY_FIVE = self.get_top_twenty_five(FortnitePlaylist.CURRENT_SOLO)
            self.CURRENT_DUO_TOP_TWENTY_FIVE = self.get_top_twenty_five(FortnitePlaylist.CURRENT_DUO)
            self.CURRENT_SQUAD_TWENTY_FIVE = self.get_top_twenty_five(FortnitePlaylist.CURRENT_SQUAD)
            self.CURRENT_SOLO_KD = self.get_kd(FortnitePlaylist.CURRENT_SOLO)
            self.CURRENT_DUO_KD = self.get_kd(FortnitePlaylist.CURRENT_DUO)
            self.CURRENT_SQUAD_KD = self.get_kd(FortnitePlaylist.CURRENT_SQUAD)
            self.CURRENT_SOLO_MATCHES = self.get_matches(FortnitePlaylist.CURRENT_SOLO)
            self.CURRENT_DUO_MATCHES = self.get_matches(FortnitePlaylist.CURRENT_DUO)
            self.CURRENT_SQUAD_MATCHES = self.get_matches(FortnitePlaylist.CURRENT_SQUAD)
            self.CURRENT_SOLO_KILLS = self.get_kills(FortnitePlaylist.CURRENT_SOLO)
            self.CURRENT_DUO_KILLS = self.get_kills(FortnitePlaylist.CURRENT_DUO)
            self.CURRENT_SQUAD_KILLS = self.get_kills(FortnitePlaylist.CURRENT_SQUAD)
            self.CURRENT_SOLO_KPG = self.get_kpg(FortnitePlaylist.CURRENT_SOLO)
            self.CURRENT_DUO_KPG = self.get_kpg(FortnitePlaylist.CURRENT_DUO)
            self.CURRENT_SQUAD_KPG = self.get_kpg(FortnitePlaylist.CURRENT_SQUAD)
            self.CURRENT_SOLO_SCORE_PER_MATCH = self.get_score_per_match(FortnitePlaylist.CURRENT_SOLO)
            self.CURRENT_DUO_SCORE_PER_MATCH = self.get_score_per_match(FortnitePlaylist.CURRENT_DUO)
            self.CURRENT_SQUAD_SCORE_PER_MATCH = self.get_score_per_match(FortnitePlaylist.CURRENT_SQUAD)

            self.LIFETIME_SOLO_SCORE = self.get_score(FortnitePlaylist.SOLO)
            self.LIFETIME_DUO_SCORE = self.get_score(FortnitePlaylist.DUO)
            self.LIFETIME_SQUAD_SCORE = self.get_score(FortnitePlaylist.SQUAD)
            self.LIFETIME_SOLO_WINS = self.get_top_one(FortnitePlaylist.SOLO)
            self.LIFETIME_DUO_WINS = self.get_top_one(FortnitePlaylist.DUO)
            self.LIFETIME_SQUAD_WINS = self.get_top_one(FortnitePlaylist.SQUAD)
            self.LIFETIME_SOLO_TOP_TWELVE = self.get_top_twelve(FortnitePlaylist.SOLO)
            self.LIFETIME_DUO_TOP_TWELVE = self.get_top_twelve(FortnitePlaylist.DUO)
            self.LIFETIME_SQUAD_TOP_TWELVE = self.get_top_twelve(FortnitePlaylist.SQUAD)
            self.LIFETIME_SOLO_TOP_TWENTY_FIVE = self.get_top_twenty_five(FortnitePlaylist.SOLO)
            self.LIFETIME_DUO_TOP_TWENTY_FIVE = self.get_top_twenty_five(FortnitePlaylist.DUO)
            self.LIFETIME_SQUAD_TWENTY_FIVE = self.get_top_twenty_five(FortnitePlaylist.SQUAD)
            self.LIFETIME_SOLO_KD = self.get_kd(FortnitePlaylist.SOLO)
            self.LIFETIME_DUO_KD = self.get_kd(FortnitePlaylist.DUO)
            self.LIFETIME_SQUAD_KD = self.get_kd(FortnitePlaylist.SQUAD)
            self.LIFETIME_SOLO_MATCHES = self.get_matches(FortnitePlaylist.SOLO)
            self.LIFETIME_DUO_MATCHES = self.get_matches(FortnitePlaylist.DUO)
            self.LIFETIME_SQUAD_MATCHES = self.get_matches(FortnitePlaylist.SQUAD)
            self.LIFETIME_SOLO_KILLS = self.get_kills(FortnitePlaylist.SOLO)
            self.LIFETIME_DUO_KILLS = self.get_kills(FortnitePlaylist.DUO)
            self.LIFETIME_SQUAD_KILLS = self.get_kills(FortnitePlaylist.SQUAD)
            self.LIFETIME_SOLO_KPG = self.get_kpg(FortnitePlaylist.SOLO)
            self.LIFETIME_DUO_KPG = self.get_kpg(FortnitePlaylist.DUO)
            self.LIFETIME_SQUAD_KPG = self.get_kpg(FortnitePlaylist.SQUAD)
            self.LIFETIME_SOLO_SCORE_PER_MATCH = self.get_score_per_match(FortnitePlaylist.SOLO)
            self.LIFETIME_DUO_SCORE_PER_MATCH = self.get_score_per_match(FortnitePlaylist.DUO)
            self.LIFETIME_SQUAD_SCORE_PER_MATCH = self.get_score_per_match(FortnitePlaylist.SQUAD)

            self.LIFETIME_KD = self.get_lifetime_kd()
            self.LIFETIME_MATCHES = self.get_lifetime_matches_played()
            self.LIFETIME_KILLS = self.get_lifetime_kills()
            self.LIFETIME_WINS = self.get_lifetime_wins()
            self.LIFETIME_SCORE = self.get_lifetime_score()
            self.LIFETIME_WIN_PERCENTAGE = self.get_lifetime_win_percentage()

    def get_score(self, playlist):
        try:
            return_data = self.json_data["stats"][playlist.value]["top10"]["value"]
        except KeyError:
            return_data = "0"
        return return_data

    def get_top_one(self, playlist):
        try:
            return_data = self.json_data["stats"][playlist.value]["top1"]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_top_twelve(self, playlist):
        try:
            return_data = self.json_data["stats"][playlist.value]["top12"]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_top_twenty_five(self, playlist):
        try:
            return_data = self.json_data["stats"][playlist.value]["top25"]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_kd(self, playlist):
        try:
            return_data = self.json_data["stats"][playlist.value]["kd"]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_matches(self, playlist):
        try:
            return_data = self.json_data["stats"][playlist.value]["matches"]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_kills(self, playlist):
        try:
            return_data = self.json_data["stats"][playlist.value]["kills"]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_kpg(self, playlist):
        try:
            return_data = self.json_data["stats"][playlist.value]["kpg"]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_score_per_match(self, playlist):
        try:
            return_data = self.json_data["stats"][playlist.value]["scorePerMatch"]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_lifetime_score(self):
        try:
            return_data = self.json_data["lifeTimeStats"][6]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_lifetime_matches_played(self):
        try:
            return_data = self.json_data["lifeTimeStats"][7]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_lifetime_wins(self):
        try:
            return_data = self.json_data["lifeTimeStats"][8]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_lifetime_win_percentage(self):
        try:
            return_data = self.json_data["lifeTimeStats"][9]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_lifetime_kills(self):
        try:
            return_data = self.json_data["lifeTimeStats"][10]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_lifetime_kd(self):
        try:
            return_data = self.json_data["lifeTimeStats"][11]["value"]
        except KeyError:
            return_data = "0"

        return return_data

    def get_epic_user_handle(self):
        try:
            return_data = self.json_data["epicUserHandle"]
        except KeyError:
            return_data = "No Epic User Handle"

        return return_data
