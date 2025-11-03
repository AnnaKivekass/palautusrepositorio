from typing import List, Optional, Callable, Any
from enum import Enum, auto
from player import Player

class SortBy(Enum):
    POINTS = auto()
    GOALS = auto()
    ASSISTS = auto()

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

    def _normalize_sort(self, sort_by) -> "SortBy":
        if isinstance(sort_by, SortBy):
            return sort_by
        if sort_by is None:
            return SortBy.POINTS
        if isinstance(sort_by, str):
            key = sort_by.strip().lower()
            if key == "points":
                return SortBy.POINTS
            if key == "goals":
                return SortBy.GOALS
            if key == "assists":
                return SortBy.ASSISTS
        raise ValueError(f"Unknown sort_by '{sort_by}'")

    def top(self, n: int, sort_by: "SortBy | str | None" = None) -> List[Player]:
        criterion = self._normalize_sort(sort_by)
        keymap: dict[SortBy, Callable[[Player], int]] = {
            SortBy.POINTS:  self._points_value,
            SortBy.GOALS:   lambda p: int(getattr(p, "goals", 0)),
            SortBy.ASSISTS: lambda p: int(getattr(p, "assists", 0)),
        }
        key = keymap[criterion]
        return sorted(self._players, key=key, reverse=True)[:n]
