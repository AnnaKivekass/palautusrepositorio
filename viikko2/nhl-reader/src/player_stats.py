from .player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality: str):
        candidates = (p for p in self._players if p.nationality == nationality)
        return sorted(candidates, key=lambda p: p.points(), reverse=True)
