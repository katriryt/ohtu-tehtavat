KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = []

    def kuuluu(self, n):
        if n in self.lukujono: 
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n): 
            self.lukujono.append(n)
            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
            return True
        return False

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return self.lukujono

    @staticmethod
    def yhdiste(a, b):
        combo_list = IntJoukko()
        list1 = a.to_int_list()
        list2 = b.to_int_list()
        list1.extend(list2)

        for i in list1: 
            combo_list.lisaa(i)

        return combo_list

    @staticmethod
    def leikkaus(a, b):
        leikkaus_lista = IntJoukko()
        list1 = a.to_int_list()
        list2 = b.to_int_list()

        for i in list1: 
            for j in list2: 
                if j == i: 
                    leikkaus_lista.lisaa(j)

        return leikkaus_lista

    @staticmethod
    def erotus(a, b):
        erotus_lista = IntJoukko()
        list1 = a.to_int_list()
        list2 = b.to_int_list()

        for i in list1: 
            erotus_lista.lisaa(i)
        
        for j in list2: 
            erotus_lista.poista(j)

        return erotus_lista

    def __str__(self):
        if len(self.lukujono) == 0:
            return "{}"

        elif len(self.lukujono) == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, len(self.lukujono) - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[len(self.lukujono) - 1])
            tuotos = tuotos + "}"
            return tuotos
