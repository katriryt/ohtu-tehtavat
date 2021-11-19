class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.all_players = self.reader.players

    def top_scorers_by_nationality(self, nationality):
        top_scorers = []

        for player in self.all_players:
            if player.nationality == nationality:
                top_scorers.append(player)

        sorted_scorers = sorted(top_scorers, key=lambda x: x.total_points, reverse=True)

        return sorted_scorers