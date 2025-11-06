"""Lukee pelaajadataa HTTP-rajapinnasta ja rakentaa Player-oliot."""

import requests
from player import Player


class PlayerReader:
    """Hakee JSON-pelaajat annetusta URL:ista."""

    def __init__(self, url: str):
        self._url = url

    def get_players(self):
        """Palauta lista Player-olioita JSON-datasta."""
        resp = requests.get(self._url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
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
