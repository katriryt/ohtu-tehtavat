KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
#    def __init__(self): #, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
#        if kapasiteetti is None:
#            self.kapasiteetti = KAPASITEETTI
#        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
#            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
#        else:
#            self.kapasiteetti = kapasiteetti

        self.kapasiteetti = kapasiteetti

#        if kasvatuskoko is None:
#            self.kasvatuskoko = OLETUSKASVATUS
#        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
#            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
#        else:
#            self.kasvatuskoko = kasvatuskoko

        self.kasvatuskoko = kasvatuskoko

        # alustaa lukujonon, voisi alustaa tyhjänä
#        self.ljono = [0] * self.kapasiteetti
        self.lukujono = []

#        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        # metodin tarkoitus on tsekata joko luku on listalla
        # palauttaa True jos on ja False jos ei ole
#        on = 0
#
#        for i in range(0, self.alkioiden_lkm):
#            if n == self.ljono[i]:
#                on = on + 1
#
#        if on > 0:
#            return True
#        else:
#            return False

        if n in self.lukujono: 
            return True
        return False

    def lisaa(self, n):
        # Metodin tarkoitus on lisätä listan loppuun annettu luku, mikäli luku ei jo ole listalla
        # LIsäksi kasvattaa alkioiden lukumäärää 1:llä, mikäli näin tehdään
#        ei_ole = 0

#        if self.alkioiden_lkm == 0:
#            self.lukujono[0] = n
#            self.alkioiden_lkm += 1
#            return True

#        else: 
        if not self.kuuluu(n): 
            self.lukujono.append(n)
#            self.alkioiden_lkm += 1
            return True
        
#        else: 
#            return False

#        if self.alkioiden_lkm == 0:
#            self.lukujono[0] = n
#            self.alkioiden_lkm = self.alkioiden_lkm + 1
#            return True
#        else:
#            pass

#        if not self.kuuluu(n):
#            self.lukujono[self.alkioiden_lkm] = n
#            self.alkioiden_lkm = self.alkioiden_lkm + 1
#
#            if self.alkioiden_lkm % len(self.lukujono) == 0:
#                taulukko_old = self.lukujono
#                self.kopioi_taulukko(self.lukujono, taulukko_old)
#                self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
#                self.kopioi_taulukko(taulukko_old, self.lukujono)

#            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
#           self.alkioiden_lkm -= 1
            return True
        return False

#        kohta = -1
#        apu = 0
#
#        for i in range(0, self.alkioiden_lkm):
#            # mikäli luku on listalla, sen kohdalle laitetaan nolla ja metodista poistutaan
#            # pythonissa voitaisiin vain popata listasta pois
#            if n == self.ljono[i]:
#                kohta = i  # siis luku löytyy tuosta kohdasta :D
#                self.ljono[kohta] = 0
#                break
#
#        if kohta != -1:
#            # jos koodissa päästään tänne asti, eli luku ei ollut listalla
#            for j in range(kohta, self.alkioiden_lkm - 1):
#                # epäselvää mitä tapahtuu
#                apu = self.ljono[j]
#                self.ljono[j] = self.ljono[j + 1]
#                self.ljono[j + 1] = apu
#
#            # vähennetään alkioiden lukumäärästä yksi
#            # tämä voitaisiin korvata len:llä
#            self.alkioiden_lkm = self.alkioiden_lkm - 1
#            return True
#
#        return False

#    def kopioi_taulukko(self, a, b):
#        # Ei käytetä testeissä mihinkään, ainoastaan kopioi taulukon kokoa
#        for i in range(0, len(a)):
#            b[i] = a[i]

    def mahtavuus(self):
        # palautetaan alkioiden lukumäärä
#        return self.alkioiden_lkm
        return len(self.lukujono)

    def to_int_list(self):
        # ilmeisesti pyritään palauttamaan lukujono listana
#        taulu = [0] * self.alkioiden_lkm
#
#        for i in range(0, len(taulu)):
#            taulu[i] = self.ljono[i]
#
#        return taulu
        return self.lukujono

    @staticmethod
    def yhdiste(a, b):
        # Tässä otetaan kaksi annettua listaa ja yhdistetään ne, palautetaan yhdistetty lista
#        x = IntJoukko()
#        a_taulu = a.to_int_list()
#        b_taulu = b.to_int_list()

#        for i in range(0, len(a_taulu)):
#            x.lisaa(a_taulu[i])
#
#        for i in range(0, len(b_taulu)):
#            x.lisaa(b_taulu[i])
#
#        return x

        combo_list = IntJoukko()
        list1 = a.to_int_list()
        list2 = b.to_int_list()
        list1.extend(list2)

        for i in list1: 
            combo_list.lisaa(i)
#        list2 = list(b)
#        list1.extend(list2)

#        a.extent(b)

        return combo_list

    @staticmethod
    def leikkaus(a, b):
        # Funktion pitäisi palauttaa mitkä luvut ovat yhteisiä
#        y = IntJoukko()
#        a_taulu = a.to_int_list()
#        b_taulu = b.to_int_list()
#
#        for i in range(0, len(a_taulu)):
#            for j in range(0, len(b_taulu)):
#                if a_taulu[i] == b_taulu[j]:
#                    y.lisaa(b_taulu[j])
#
#        return y

#        leikkaus_lista_raw = []
        leikkaus_lista = IntJoukko()
        list1 = a.to_int_list()
        list2 = b.to_int_list()

        for i in list1: 
            for j in list2: 
                if j == i: 
#                    leikkaus_lista_raw.append(j)
                    leikkaus_lista.lisaa(j)

#        leikkaus_lista_raw.sort()

#        leikkaus_lista = IntJoukko()

#        for luku in leikkaus_lista_raw:
#            leikkaus_lista.lisaa(luku)

        return leikkaus_lista

    @staticmethod
    def erotus(a, b):
        # Funktion pitäisi palauttaa mitkä luvut eivät ole yhteisiä
#        z = IntJoukko()
#        a_taulu = a.to_int_list()
#        b_taulu = b.to_int_list()
#
#        for i in range(0, len(a_taulu)):
#            z.lisaa(a_taulu[i])
#
#        for i in range(0, len(b_taulu)):
#            z.poista(b_taulu[i])
#
#        return z

        erotus_lista = IntJoukko()
        list1 = a.to_int_list()
        list2 = b.to_int_list()

        for i in list1: 
            erotus_lista.lisaa(i)
        
        for j in list2: 
            erotus_lista.poista(j)

        return erotus_lista

    def __str__(self):
        # tulostus
#        if self.alkioiden_lkm == 0:
        if len(self.lukujono) == 0:
            return "{}"
#        elif self.alkioiden_lkm == 1:
        elif len(self.lukujono) == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
#            for i in range(0, self.alkioiden_lkm - 1):
            for i in range(0, len(self.lukujono) - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
#            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + str(self.lukujono[len(self.lukujono) - 1])
            tuotos = tuotos + "}"
            return tuotos
