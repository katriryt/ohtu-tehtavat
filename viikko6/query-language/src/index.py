from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, Or, All

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # Annettu alkuperäinen kysely
#    matcher = And(
#        HasAtLeast(5, "goals"),
#        HasAtLeast(5, "assists"),
#        PlaysIn("PHI")
#    )

# Tehtävä 2: testaa, että palauttaa Not, toimii
#    matcher = And(
#        Not(HasAtLeast(1, "goals")),
#        PlaysIn("NYR")
#    )

    # tehtävä 2: testattu, että All toimii, OK
#    matcher = All()

#    matcher = And(
#        HasAtLeast(1, "goals"),
#        PlaysIn("NYR")
#    )
#
#
    # Tehtävä 2: testaa, että palauttaa FewerThan, toimii
#    matcher = And(
#        HasFewerThan(1, "goals"),
#        PlaysIn("NYR")
#    )

    # Tehtävä 3: Testaa Or-luokan toimintaa. toimii.
#    matcher = Or(
#        HasAtLeast(30, "goals"),
#        HasAtLeast(50, "assists")
#    )

    # Tehtävä 3: Testaa Or luokan toimintaa, toimii
    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
