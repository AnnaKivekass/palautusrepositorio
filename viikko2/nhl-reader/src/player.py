class Player:
    def __init__(self, data: dict):
        self.name = data.get("name", "")
        self.nationality = data.get("nationality", "")
        self.team = data.get("team", "")
        self.goals = int(data.get("goals", 0))
        self.assists = int(data.get("assists", 0))

    def points(self) -> int:
        return self.goals + self.assists

    def __str__(self) -> str:
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.points()}"
