import requests
from player import Player

class PlayerReader:
    def __init__(self,url):
        self.response = requests.get(url).json()
#        print("JSON-muotoinen vastaus:")
#        print(self.response)
        self.players = []
        self.form_players()

    def form_players(self):
        for player_dict in self.response:
            player = Player(
                player_dict['name'], 
                player_dict['team'], 
                player_dict['goals'], 
                player_dict['assists'], 
                player_dict['nationality']
            )

            self.players.append(player)
