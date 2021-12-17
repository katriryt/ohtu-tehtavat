# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = []

        self._tekoalyn_muisti_laskuri = {
            "k": 0,
            "p": 0,
            "s": 0
        }

        self._tekoalyn_vastaus = {
            "k": "p",
            "p": "s",
        } 

    def aseta_siirto(self, siirto):
        self._muisti.append(siirto)

    def anna_siirto(self):
        if len(self._muisti) <= 1: 
            return "k"

        self.tekoalyn_laskelma()

        if len(list(set(list(self._tekoalyn_muisti_laskuri.values())))) == 1:
            return "k"
        else: 
            suurin_avain = max(self._tekoalyn_muisti_laskuri, key=self._tekoalyn_muisti_laskuri.get)
            if suurin_avain in self._tekoalyn_vastaus:
                return self._tekoalyn_vastaus[suurin_avain]
            else: 
                return "k"

    def tekoalyn_laskelma(self):
        self._tekoalyn_muisti_laskuri = {"k": 0, "p": 0, "s": 0}

        viimeisin_siirto = self._muisti[-1]

        for i in range(0, len(self._muisti)-1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]
                if seuraava == "k":
                    self._tekoalyn_muisti_laskuri["k"] += 1
                elif seuraava == "p":
                    self._tekoalyn_muisti_laskuri["p"] += 1
                else:
                    self._tekoalyn_muisti_laskuri["s"] += 1
