from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.kori = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        lukumaara = 0
        for item in self.kori: 
            lukumaara += item.lukumaara()
        return lukumaara

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        yhteishinta = 0
        for item in self.kori:
            yhteishinta += item.hinta()
        return yhteishinta

    def lista_korin_nimistä(self): 
        nimi_lista = []
        for item in self.kori: 
            nimi_lista.append(item.tuotteen_nimi())
        return nimi_lista

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        tuotteen_nimi = lisattava.nimi()
        if tuotteen_nimi not in self.lista_korin_nimistä(): 
            self.kori.append(Ostos(lisattava))
        else: 
            for item in self.kori: 
                if tuotteen_nimi == item.tuotteen_nimi():
                    item.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        tuotteen_nimi = poistettava.nimi()
        if tuotteen_nimi in self.lista_korin_nimistä(): 
            for item in self.kori: 
                if tuotteen_nimi == item.tuotteen_nimi():
                    item.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        if self.tavaroita_korissa() == 0: 
            self.kori = []
        return self.kori
