import requests
from .player import Player

class PlayerReader:
    def __init__(self, url: str):
        self.url = url

    def get_players(self):
        data = requests.get(self.url).json()
        return [Player(d) for d in data]
