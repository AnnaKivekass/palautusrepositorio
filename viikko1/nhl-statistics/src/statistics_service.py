from typing import List, Optional, Callable, Any
from player import Player

class StatisticsService:
    def __init__(self, reader):
        self._reader = reader
        self._players: List[Player] = reader.get_players()

    def search(self, name: str) -> Optional[Player]:
        for p in self._players:
            if p.name == name:
                return p
        return None

    def team(self, team: str) -> List[Player]:
        return [p for p in self._players if p.team == team]

    def _points_value(self, p: Player) -> int:
        val: Any = getattr(p, "points", None)
        if callable(val):
            try:
                return int(val())
            except Exception:
                pass
        if isinstance(val, (int, float)):
            return int(val)
        return int(getattr(p, "goals", 0)) + int(getattr(p, "assists", 0))

    def top(self, n: int, sort_by: str = "points") -> List[Player]:
        keymap: dict[str, Callable[[Player], int]] = {
            "points":  self._points_value,
            "goals":   lambda p: int(getattr(p, "goals", 0)),
            "assists": lambda p: int(getattr(p, "assists", 0)),
        }
        sort_key = sort_by.lower()
        key = keymap[sort_key]
        return sorted(self._players, key=key, reverse=True)[:n]
