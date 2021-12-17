# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
#        print("luo paremman tekoälyn")
        self._muisti = []
#        self._muisti = [None] * muistin_koko # voidaan alustaa pythonissa tyhjänä
#        self._vapaa_muisti_indeksi = 0 # ei tarvetta tälle pythonissa

#        self._suurinta_seuraava_siirto = {
#            "k": "p", 
#            "p": "s",
#        }

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
        # jos muisti täyttyy, unohdetaan viimeinen alkio
        # oma: pythonissa ei tarvetta tällaiselle. voidaan vain lisätä muisti-listan loppuun
 #       if self._vapaa_muisti_indeksi == len(self._muisti):
 #           for i in range(1, len(self._muisti)):
 #               self._muisti[i - 1] = self._muisti[i]

#            self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi - 1

#        self._muisti[self._vapaa_muisti_indeksi] = siirto
        self._muisti.append(siirto)
#        self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi + 1 # ei tarpeen, poista

    def anna_siirto(self):
#        print("paremman tekiälyn siirrossa")
#        if self._vapaa_muisti_indeksi == 0 or self._vapaa_muisti_indeksi == 1: # ensimmäiset kaksi on kiveä
#            print("ekat kaksi aina kiveä")
#            return "k"

        if len(self._muisti) <= 1: 
            return "k"

#        print(f"tekoälyn muistissa: {self._muisti}")
#        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1] # saa pythonissa helpomminkin, haetaan vain viimeisin listalta
#        print(viimeisin_siirto)

        self.tekoalyn_laskelma()

#        viimeisin_siirto = self._muisti[-1]
#        print(viimeisin_siirto)
#
##        k = 0
##        p = 0
##        s = 0
#
#
#        self._tekoalyn_muisti_laskuri = {"k": 0, "p": 0, "s": 0
#        }
#
#        for i in range(0, len(self._muisti)-1): # tässä lasketaan mitä on käytetty eniten
##        for i in range(0, self._vapaa_muisti_indeksi - 1): # tässä lasketaan mitä on käytetty eniten
##            print(i)
#            if viimeisin_siirto == self._muisti[i]: # jos viimeisin on sama kuin listalta haettu
#                print("nyt huomioidaan siirto")
#                seuraava = self._muisti[i + 1]
#                print(f"seuraava listalla on: {seuraava}")
#                if seuraava == "k":
##                    k = k + 1
##                    k += 1
#                    self._tekoalyn_muisti_laskuri["k"] += 1
#                elif seuraava == "p":
##                    p += 1
#                    self._tekoalyn_muisti_laskuri["p"] += 1
#                else:
##                    s += 1
#                    self._tekoalyn_muisti_laskuri["s"] += 1
#
##        print(f"tekoälyn laskelmat: k:{k}, p:{p}, s:{s}")
#        print(self._tekoalyn_muisti_laskuri)
        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi

#        print(f"suurin on: {max(k, p, s)}")

        if len(list(set(list(self._tekoalyn_muisti_laskuri.values())))) == 1:
#            print("kaikki arvot samoja")
            return "k"
        else: 
            suurin_avain = max(self._tekoalyn_muisti_laskuri, key=self._tekoalyn_muisti_laskuri.get)
#            print(suurin_avain)
            if suurin_avain in self._tekoalyn_vastaus:
                return self._tekoalyn_vastaus[suurin_avain]
            else: 
                return "k"

#        if k > p or k > s:
#            print(f"k oli suurin, palauttaa {self._tekoalyn_vastaus['k']}")
#            return "p"
#        elif p > k or p > s:
#            print(f"p oli suurin, palauttaa {self._tekoalyn_vastaus['p']}")
#            return "s"
#        else:
#            print("palauttaa k")
#            return "k"

    def tekoalyn_laskelma(self):
        self._tekoalyn_muisti_laskuri = {"k": 0, "p": 0, "s": 0}
#        print(self._tekoalyn_muisti_laskuri)

        viimeisin_siirto = self._muisti[-1]
#        print(viimeisin_siirto)

        for i in range(0, len(self._muisti)-1): # tässä lasketaan mitä on käytetty eniten
#        for i in range(0, self._vapaa_muisti_indeksi - 1): # tässä lasketaan mitä on käytetty eniten
#            print(i)
            if viimeisin_siirto == self._muisti[i]: # jos viimeisin on sama kuin listalta haettu
#                print("nyt huomioidaan siirto")
                seuraava = self._muisti[i + 1]
#                print(f"seuraava listalla on: {seuraava}")
                if seuraava == "k":
#                    k = k + 1
#                    k += 1
                    self._tekoalyn_muisti_laskuri["k"] += 1
                elif seuraava == "p":
#                    p += 1
                    self._tekoalyn_muisti_laskuri["p"] += 1
                else:
#                    s += 1
                    self._tekoalyn_muisti_laskuri["s"] += 1

#        print(f"tekoälyn laskelmat: k:{k}, p:{p}, s:{s}")
#        print(self._tekoalyn_muisti_laskuri)