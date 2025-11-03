import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53), 
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
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
        self.assertIsNone(self.stats.search("Not A Player"))

    def test_team_filters_by_team(self):
        names = {p.name for p in self.stats.team("EDM")}
        self.assertEqual(names, {"Semenko", "Kurri", "Gretzky"})

    def test_team_empty_when_no_matches(self):
        self.assertEqual(self.stats.team("XYZ"), [])

    def test_top_default_points(self):
        top3 = self.stats.top(3)
        self.assertEqual([p.name for p in top3], ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_by_goals(self):
        top2 = self.stats.top(2, "goals")
        self.assertEqual([p.name for p in top2], ["Lemieux", "Yzerman"])

    def test_top_by_assists(self):
        top2 = self.stats.top(2, "assists")
        self.assertEqual([p.name for p in top2], ["Gretzky", "Yzerman"])

    def test_top_invalid_sort_by_raises(self):
        with self.assertRaises(ValueError):
            self.stats.top(1, "invalid_key")

if __name__ == "__main__":
    unittest.main()
