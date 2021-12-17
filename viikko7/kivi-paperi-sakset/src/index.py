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
        peli_tapahtuma = Pelitehdas()
        peli = peli_tapahtuma.hae(vastaus)
        if peli is None: 
            break
        peli.pelaa()

if __name__ == "__main__":
    main()
