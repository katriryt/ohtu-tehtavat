from player_reader import PlayerReader
from player_stats import PlayerStats
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    country = 'FIN'
    players = stats.top_scorers_by_nationality(country)
    print(f"Players from {country} {datetime.now()} \n")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
