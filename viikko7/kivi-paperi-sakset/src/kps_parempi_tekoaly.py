#from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

#class KPSParempiTekoaly:
#    def pelaa(self):
#        tuomari = Tuomari() # ylilyokassa
#        tekoaly = TekoalyParannettu(10) # konstruktoriin
#
#        ekan_siirto = input("Ensimmäisen pelaajan siirto: ") # ylilyokassa
#        tokan_siirto = tekoaly.anna_siirto() #_toisen_siirto -metodissa
#
#        print(f"Tietokone valitsi: {tokan_siirto}") #_toisen_siirto -metodissa
#
#        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto): # yliluokassa
#            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto) # yliluokassa
#            print(tuomari) # yliluokassa
#
#            ekan_siirto = input("Ensimmäisen pelaajan siirto: ") # yliluokassa
#            tokan_siirto = tekoaly.anna_siirto() # _toisen_siirto -metodissa
#
#            print(f"Tietokone valitsi: {tokan_siirto}") # _toisen_siirto -metodissa
#            tekoaly.aseta_siirto(ekan_siirto) # _toisen_siirto -metodissa
#
#        print("Kiitos!") # yliluokassa
#        print(tuomari) # yliluokassa
#
#    def _onko_ok_siirto(self, siirto): # yliluokassa
#        return siirto == "k" or siirto == "p" or siirto == "s" # yliluokassa

class KPSParempiTekoaly(KPS): # perii yliluokan
    # toteutetaan metodi pelityypin mukaisesti
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)

        return tokan_siirto