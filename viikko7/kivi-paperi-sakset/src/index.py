#from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
#from kps_tekoaly import KPSTekoaly
#from kps_parempi_tekoaly import KPSParempiTekoaly
from pelitehdas import Pelitehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()[-1]
#        print(vastaus)
#        vastaus2 = vastaus[-1]
#        print(vastaus2)
        peli_tapahtuma = Pelitehdas()
#        print(peli)
        peli = peli_tapahtuma.hae(vastaus)
#        print(peli2)
        if peli is None: 
            break
        peli.pelaa()

#        if vastaus.endswith("a"):
#            print(
#                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
#            )
#
#            kaksinpeli = KPSPelaajaVsPelaaja()
#            kaksinpeli.pelaa() # toteutettu template-metodina
#        elif vastaus.endswith("b"):
#            print(
#                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
#            )
#
#            yksinpeli = KPSTekoaly()
#            yksinpeli.pelaa() # toteutettu template-metodina
#        elif vastaus.endswith("c"):
#            print(
#                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
#            )
#            print("haastavammassa pelissä")
#            haastava_yksinpeli = KPSParempiTekoaly() # toteutettu template-metodina
#            haastava_yksinpeli.pelaa()
#        else:
#            break


if __name__ == "__main__":
    main()
