"""Player-tietoluokka."""

class Player:
    """Pelaajan olennaiset kentät ja johdetut pisteet."""

    def __init__(self, name: str, team: str, goals: int, assists: int, nationality: str):
        self.name = name
        self.team = team
        self.goals = int(goals)
        self.assists = int(assists)
        self.nationality = nationality

    @property
    def points(self) -> int:
        """Palauta pisteet = maalit + syötöt."""
        return self.goals + self.assists
