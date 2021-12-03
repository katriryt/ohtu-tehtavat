# refaktoroi: jaa moniin pieniin metodeihin, jotka nimennällään palstavatoman toimintalogiikkansa

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

#        self.even_messages = {0: "Love-All",
#                            1: "Fifteen-All",
#                            2: "Thirty-All",
#                            3: "Forty-All"
#                            }

        self.win_messages = {1: "Advantage player1", 
                            -1: "Advantage player2",
                            2: "Win for player1", 
                            -2: "Win for player2", 
                            3: "Win for player1",
                            -3: "Win for player2",
                            4: "Win for player1",
                            -4: "Win for player2",
                            }

        self.normal_message = {0: "Love", 
                            1: "Fifteen",
                            2: "Thirty",
                            3: "Forty"
        }

    def won_point(self, player_name):
#        if player_name == "player1":
        if player_name == self.player1_name:
#            self.m_score1 = self.m_score1 + 1 # voi lyhentää
            self.m_score1 += 1
        else:
#            self.m_score2 = self.m_score2 + 1
            self.m_score2 += 1

    def score_when_even(self): 
#        score = ""
#        if self.m_score1 == 0: # tee sanakirja
#            score = "Love-All"
#        elif self.m_score1 == 1:
#            score = "Fifteen-All"
#        elif self.m_score1 == 2:
#            score = "Thirty-All"
#        elif self.m_score1 == 3:
#            score = "Forty-All"
#        else:
#            score = "Deuce"

#        if self.m_score1 in self.even_messages:
        if self.m_score1 in self.normal_message:
#            return self.even_messages[self.m_score1]
            return f"{self.normal_message[self.m_score1]}-All"
        else:
            return "Deuce"

#        return score

    def score_when_more_than_4_points(self):
#        score = ""
#        minus_result = self.m_score1 - self. m_score2
#        if minus_result == 1:
#            score = "Advantage player1"
#        elif minus_result == -1:
#            score = "Advantage player2"
#        elif minus_result >= 2:
#            score = "Win for player1"
#        else:
#            score = "Win for player2"

#        if minus_result in self.win_messages:
#        return self.win_messages[minus_result]
        return self.win_messages[self.m_score1 - self. m_score2]

#        return score

    def score_when_game_continues(self):
#        score = ""
#        temp_score = 0
#        for i in range(1, 3): # katsoo vain ykkös- ja kakkospelaajille, ensin ykköspelaajan pisteet, sitten kakkospelaajan pisteet
#            if i == 1:
#                temp_score = self.m_score1
#            else:
#                score = score + "-"
#                temp_score = self.m_score2
#            if temp_score == 0:
#                score = score + "Love"
#            elif temp_score == 1:
#                score = score + "Fifteen"
#            elif temp_score == 2:
#                score = score + "Thirty"
#            elif temp_score == 3:
#                score = score + "Forty"

#        return score

        return f"{self.normal_message[self.m_score1]}-{self.normal_message[self.m_score2]}"

    def get_score(self):
        score = ""
#        temp_score = 0

        # ehkä voi tehdä lopuksi erillisen metodin tilanteen tsekkaamiseen

        if self.m_score1 == self.m_score2: # jos ollaan tasapelissä
            score = self.score_when_even()
            # yksi metodi: palauttaa sanakirjasta 
#            if self.m_score1 == 0: # tee sanakirja
#                score = "Love-All"
#            elif self.m_score1 == 1:
#                score = "Fifteen-All"
#            elif self.m_score1 == 2:
#                score = "Thirty-All"
#            elif self.m_score1 == 3:
#                score = "Forty-All"
#            else:
#                score = "Deuce"
        elif self.m_score1 >= 4 or self.m_score2 >= 4: # jos toisella on neljä tai yli pisteitä
            # toinen metodi: kun yli neljä kierrosta, palauttaa tilanteen, tässä toinen kirjasto
            score = self.score_when_more_than_4_points()
#            minus_result = self.m_score1 - self. m_score2
#
#            if minus_result == 1:
#                score = "Advantage player1"
#            elif minus_result == -1:
#                score = "Advantage player2"
#            elif minus_result >= 2:
#                score = "Win for player1"
#            else:
#                score = "Win for player2"

        else: # jos ei olla tasapelissä eikä yli neljässä pallossa
            # kolmas metodi: ekan vs. tokan jampan pisteet, laitetaanyhteen, dictionary
#            for i in range(1, 3): # katsoo vain ykkös- ja kakkospelaajille, ensin ykköspelaajan pisteet, sitten kakkospelaajan pisteet
#                if i == 1:
#                    temp_score = self.m_score1
#                else:
#                    score = score + "-"
#                    temp_score = self.m_score2
#
#                if temp_score == 0:
#                    score = score + "Love"
#                elif temp_score == 1:
#                    score = score + "Fifteen"
#                elif temp_score == 2:
#                    score = score + "Thirty"
#                elif temp_score == 3:
#                    score = score + "Forty"

            score = self.score_when_game_continues()

        return score
