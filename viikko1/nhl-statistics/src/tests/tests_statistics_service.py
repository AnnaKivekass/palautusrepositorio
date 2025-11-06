import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),    # 16
            Player("Lemieux", "PIT", 45, 54),  # 99
            Player("Kurri",   "EDM", 37, 53),  # 90
            Player("Yzerman", "DET", 42, 56),  # 98
            Player("Gretzky", "EDM", 35, 89),  # 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_found(self):
        p = self.stats.search("Gretzky")
        self.assertIsNotNone(p)
        self.assertEqual(p.name, "Gretzky")
        self.assertEqual(p.team, "EDM")

    def test_search_not_found(self):
        self.assertIsNone(self.stats.search("Nope"))

    def test_team_filters(self):
        names = {p.name for p in self.stats.team("EDM")}
        self.assertEqual(names, {"Semenko", "Kurri", "Gretzky"})

    def test_team_empty(self):
        self.assertEqual(self.stats.team("XYZ"), [])

    def test_top_default_is_points(self):
        top3 = self.stats.top(3)  # default
        self.assertEqual([p.name for p in top3], ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_points_enum(self):
        top3 = self.stats.top(3, SortBy.POINTS)
        self.assertEqual([p.name for p in top3], ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_goals_enum(self):
        top2 = self.stats.top(2, SortBy.GOALS)
        self.assertEqual([p.name for p in top2], ["Lemieux", "Yzerman"])

    def test_top_assists_enum(self):
        top2 = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual([p.name for p in top2], ["Gretzky", "Yzerman"])

    def test_top_accepts_legacy_strings(self):
        self.assertEqual([p.name for p in self.stats.top(2, "goals")], ["Lemieux", "Yzerman"])
        self.assertEqual([p.name for p in self.stats.top(2, "assists")], ["Gretzky", "Yzerman"])
        self.assertEqual([p.name for p in self.stats.top(2, "points")], ["Gretzky", "Lemieux"])

    def test_top_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.stats.top(1, "invalid_key")

if __name__ == "__main__":
    unittest.main()
