import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    # step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # step 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuoteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    # step 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipa", 5)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 5
    def test_kaksi_tuotetta_lisatty_ostoskorin_hinta_histojen_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipa", 5)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(self.kori.hinta(), 8)

    # step 6: 
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 7:
    def test_kaksi_samaa_tuotetta_lisatty_ostoskorin_hinta_hintojen_tupla(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 2*3)

    # step 8: 
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
 
        # testaa että metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)

    # step 9:
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        nimi = ostos.tuotteen_nimi()
        maara = ostos.lukumaara() 

        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        self.assertEqual(("Maito", 1), (nimi, maara))

    # step 10: 
    def test_kaksi_eri_tuotetta_lisatty_korissa_kaksi_ostosta(self):        
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        leipa = Tuote("Leipa", 5)
        self.kori.lisaa_tuote(leipa)
        
        ostokset = self.kori.ostokset()
 
        self.assertEqual(len(ostokset), 2)

    # step 11: 
    def test_kaksi_samaa_tuotetta_lisatty_korissa_kaksi_ostosta(self):        
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

        self.assertEqual(len(self.kori.ostokset()), 1)

    # step 12: 
    def test_kaksi_samaa_tuotetta_korissa_sama_nimi_maara_kaksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        
        ostos = self.kori.ostokset()[0]
        nimi = ostos.tuotteen_nimi()
        maara = ostos.lukumaara() 
 
        self.assertEqual(("Maito", 2), (nimi, maara))

    # step 13: 
    def test_kaksi_samaa_tuotetta_poistetaan_yksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        
        ostos = self.kori.ostokset()[0]
        nimi = ostos.tuotteen_nimi()
        maara = ostos.lukumaara() 
 
        self.assertEqual(("Maito", 1), (nimi, maara))
