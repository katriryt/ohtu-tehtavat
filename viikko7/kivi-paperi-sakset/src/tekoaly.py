class Tekoaly:
    def __init__(self):
#        print("luodaan tekoäly")
        self._siirto = 0

    def anna_siirto(self):
        # OMA: tälle voi kokeilla kirjastoa, muuten ok
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
#            print("tietokone on nollan jakojäännöksessä")
            return "k"
        elif self._siirto == 1:
#            print("tietokone on yhden jakojäännöksessä")
            return "p"
        else:
#            print("tietokone on muussa jakojäännöksessä")
            return "s"

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
