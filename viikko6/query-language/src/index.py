from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, Or, All, QueryBuilder

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

# Tehtävä 2: testaa, että palauttaa Not
#    matcher = And(
#        Not(HasAtLeast(1, "goals")),
#        PlaysIn("NYR")
#    )

# Tehtävä 2: testattu, että All toimii
#    matcher = All()

#    matcher = And(
#        HasAtLeast(1, "goals"),
#        PlaysIn("NYR")
#    )
#
#
# Tehtävä 2: testaa, että palauttaa FewerThan
#    matcher = And(
#        HasFewerThan(1, "goals"),
#        PlaysIn("NYR")
#    )

    # Tehtävä 3: Testaa Or-luokan toimintaa
#    matcher = Or(
#        HasAtLeast(30, "goals"),
#        HasAtLeast(50, "assists")
#    )

# Tehtävä 3: Testaa Or luokan toimintaa
#    matcher = And(
#        HasAtLeast(40, "points"),
#        Or(
#            PlaysIn("NYR"),
#            PlaysIn("NYI"),
#            PlaysIn("BOS")
#        )
#    )

# Tehtävä 4: Parannettu kyselykieli, 1
    query = QueryBuilder()
    # Tehtävä 4.1: Palauttaa kaikki pelaajat
#    matcher = query.build()

    # Tehtävä 4.2: palauttaa pelaajat, joiden joukkue on NYR
#    matcher = query.playsIn("NYR").build()

    # Tehtävä 4.3: palauttaa NYR ja tietyt maalit
#    matcher = query.hasAtLeast(5, "goals").build()
#    matcher = query.hasFewerThan(10, "goals").build()
#    matcher = query.hasAtLeast(5, "goals").playsIn("NYR").build()
#    matcher = query.playsIn("NYR").hasAtLeast(5, "goals").build()
#    matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasFewerThan(10, "goals").build()

    matcher = (
        query
        .playsIn("NYR")
        .hasAtLeast(5, "goals")
        .hasFewerThan(10, "goals")
        .build()
    )

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
