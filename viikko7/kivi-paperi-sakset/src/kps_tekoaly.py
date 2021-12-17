#from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KPS

#class KPSTekoaly:
#    def pelaa(self):
#        tuomari = Tuomari() # yliluokassa
#        tekoaly = Tekoaly() # _toisen_siirto -metodiin
#
#        ekan_siirto = input("Ensimmäisen pelaajan siirto: ") # yliluokassa
#        tokan_siirto = tekoaly.anna_siirto() # # _toisen_siirto -metodiin
#
#        print(f"Tietokone valitsi: {tokan_siirto}") # _toisen_siirto -metodiin
#
#        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto): #yliluokassa
#            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto) #yliluokassa
#            print(tuomari) #yliluokassa
#
#            ekan_siirto = input("Ensimmäisen pelaajan siirto: ") #yliluokassa
#            tokan_siirto = tekoaly.anna_siirto() #_toisen_siirto -metodissa
#
#            print(f"Tietokone valitsi: {tokan_siirto}") #yliluokassa TÄMÄN VOI LAITTAA KIRJATOKSIA, VARIOIDAAN VIESTIÄ
#
#        print("Kiitos!") #yliluokassa
#        print(tuomari) #yliluokassa
#    def _onko_ok_siirto(self, siirto): # yliluokassa
#        return siirto == "k" or siirto == "p" or siirto == "s"

class KPSTekoaly(KPS): # perii yliluokan
    # toteutetaan metodi pelityypin mukaisesti
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto