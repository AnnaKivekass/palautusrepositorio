class Player:
    def __init__(self, player_dict):
        self.name = player_dict.get("name", "")
        self.team = player_dict.get("team", "")
        self.goals = player_dict.get("goals", 0)
        self.assists = player_dict.get("assists", 0)
        self.nationality = player_dict.get("nationality", "")

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = {self.points():2}"
