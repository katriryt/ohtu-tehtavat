import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_name_found(self):
        response = self.statistics.search("Semenko")
#        print(response)
#        wanted_response = f"Semenko EDM 4 + 12 = 16"
#        self.assertEqual(response, wanted_response)
        self.assertEqual(response.name, "Semenko")

    def test_search_no_name(self):
        response = self.statistics.search("Jimmy")
        self.assertEqual(response, None)
    
    def test_team_list(self):
        response = self.statistics.team("EDM")
        self.assertEqual(len(response), 3)
    
    def test_top_scorers_list(self):
        response = self.statistics.top_scorers(2)
        self.assertEqual(len(response), 3)