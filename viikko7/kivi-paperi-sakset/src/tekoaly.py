class Tekoaly:
    def __init__(self):
#        print("luodaan tekoäly")
        self._siirto = 0

        self._siirrot = {
            0: "k", 
            1: "p",
        }

    def anna_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

#        print(f"anna siirrossa: siirto on {self._siirto}")

        if self._siirto in self._siirrot: 
#            print(f"palauttaa komentoa {self._siirrot[self._siirto]}")
            return self._siirrot[self._siirto]
        else:
#            print("palauttaa s:ää")
            return "s"

#        if self._siirto == 0:
##            print("tietokone on nollan jakojäännöksessä")
#            return "k"
#        elif self._siirto == 1:
##            print("tietokone on yhden jakojäännöksessä")
#            return "p"
#        else:
##            print("tietokone on muussa jakojäännöksessä")
#            return "s"

#    def aseta_siirto(self, siirto):
        # ei tehdä mitään
#        pass
