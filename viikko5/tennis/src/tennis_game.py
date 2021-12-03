# refaktoroi: jaa moniin pieniin metodeihin, jotka nimennällään palstavatoman toimintalogiikkansa

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

        self.win_messages = {1: f"Advantage {self.player1_name}", 
                            -1: f"Advantage {self.player2_name}",
                             2: f"Win for {self.player1_name}", 
                            -2: f"Win for {self.player2_name}", 
                             3: f"Win for {self.player1_name}",
                            -3: f"Win for {self.player2_name}",
                             4: f"Win for {self.player1_name}",
                            -4: f"Win for {self.player2_name}",
                            }

        self.normal_message = {0: "Love", 
                            1: "Fifteen",
                            2: "Thirty",
                            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def score_when_even(self): 
        if self.m_score1 in self.normal_message:
            return f"{self.normal_message[self.m_score1]}-All"
        else:
            return "Deuce"

    def score_when_more_than_4_points(self):
        return self.win_messages[self.m_score1 - self. m_score2]

    def score_when_game_continues(self):
        return f"{self.normal_message[self.m_score1]}-{self.normal_message[self.m_score2]}"

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = self.score_when_even()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.score_when_more_than_4_points()

        else:
            score = self.score_when_game_continues()

        return score
