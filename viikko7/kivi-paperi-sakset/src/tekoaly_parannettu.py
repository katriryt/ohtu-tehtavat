# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
#        print("luo paremman tekoälyn")
        self._muisti = [None] * muistin_koko # voidaan alustaa pythonissa tyhjänä
        self._vapaa_muisti_indeksi = 0 # ei tarvetta tälle pythonissa

    def aseta_siirto(self, siirto):
        # jos muisti täyttyy, unohdetaan viimeinen alkio
        # oma: pythonissa ei tarvetta tällaiselle. voidaan vain lisätä muisti-listan loppuun
        if self._vapaa_muisti_indeksi == len(self._muisti):
            for i in range(1, len(self._muisti)):
                self._muisti[i - 1] = self._muisti[i]

            self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi - 1

        self._muisti[self._vapaa_muisti_indeksi] = siirto
        self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi + 1

    def anna_siirto(self):
#        print("paremman tekiälyn siirrossa")
        if self._vapaa_muisti_indeksi == 0 or self._vapaa_muisti_indeksi == 1: # ensimmäiset kaksi on kiveä
#            print("ekat kaksi aina kiveä")
            return "k"

        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1] # saa pythonissa helpomminkin, haetaan vain viimeisin listalta

        k = 0
        p = 0
        s = 0

#        print(f"tekoälyn muistissa: {self._muisti}")

        for i in range(0, self._vapaa_muisti_indeksi - 1): # tässä lasketaan mitä on käytetty eniten
#            print(i)
            if viimeisin_siirto == self._muisti[i]: # jos viimeisin on sama kuin listalta haettu
#                print("nyt huomioidaan siirto")
                seuraava = self._muisti[i + 1]

                if seuraava == "k":
                    k = k + 1
                elif seuraava == "p":
                    p = p + 1
                else:
                    s = s + 1

#        print(f"tekoälyn laskelmat: k:{k}, p:{p}, s:{s}")
        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p or k > s:
            return "p"
        elif p > k or p > s:
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
