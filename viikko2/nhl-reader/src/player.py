class Player:
    def __init__(self, name: str, team: str, goals: int, assists: int, nationality: str):
        self.name = name
        self.team = team
        self.goals = int(goals)
        self.assists = int(assists)
        self.nationality = nationality

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:5} {self.goals:2} + {self.assists:2} = {self.points:3}"
