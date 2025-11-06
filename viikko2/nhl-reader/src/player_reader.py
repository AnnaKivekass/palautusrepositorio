import requests
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        self._url = url

    def get_players(self):
        resp = requests.get(self._url, timeout=15)
        resp.raise_for_status()

        data = resp.json()
        if not isinstance(data, list):
            raise ValueError(f"Unexpected payload from {self._url}: expected list")

        players = []
        for p in data:
            if not isinstance(p, dict):
                continue
            players.append(
                Player(
                    p.get("name", ""),
                    p.get("team", ""),
                    int(p.get("goals", 0)),
                    int(p.get("assists", 0)),
                    p.get("nationality", ""),
                )
            )
        return players
