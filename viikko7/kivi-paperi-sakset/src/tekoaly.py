class Tekoaly:
    def __init__(self):
        self._siirto = 0

        self._siirrot = {
            0: "k", 
            1: "p",
        }

    def anna_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto in self._siirrot: 
            return self._siirrot[self._siirto]
        else:
            return "s"
