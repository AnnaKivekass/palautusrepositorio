class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = [p for p in self._reader.get_players() if p.nationality.upper() == nationality.upper()]
        players.sort(key=lambda p: p.points, reverse=True)
        return players
