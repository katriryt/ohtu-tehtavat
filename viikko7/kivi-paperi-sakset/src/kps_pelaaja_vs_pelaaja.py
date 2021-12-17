#from tuomari import Tuomari
from kps import KPS

#class KPSPelaajaVsPelaaja:
#    def pelaa(self): # tämä funktio on kokonaan yliluokassa
#        tuomari = Tuomari() # yliluokassa
#
#        ekan_siirto = input("Ensimmäisen pelaajan siirto: ") # yliluokassa
#        tokan_siirto = input("Toisen pelaajan siirto: ") # yliluokassa
#
#        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto): # yliluokassa
#            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto) # yliluokassa
#            print(tuomari) # yliluokassa
#
#            ekan_siirto = input("Ensimmäisen pelaajan siirto: ") # yliluokassa
#            tokan_siirto = input("Toisen pelaajan siirto: ") # yliluokassa
#
#        print("Kiitos!") # yliluokassa
#        print(tuomari) # yliluokassa
#
#    def _onko_ok_siirto(self, siirto): # tämäkin on kokonaan yliluokassa
#        return siirto == "k" or siirto == "p" or siirto == "s"

class KPSPelaajaVsPelaaja(KPS): # perii yliluokan
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto
