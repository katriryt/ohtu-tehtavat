from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Pelitehdas:
    def __init__(self):
        self.komennot = {
            "a": KPSPelaajaVsPelaaja(), 
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly()
        }

    def hae(self, komento):
        if komento in self.komennot: 
            return self.komennot[komento]
        else:
            return None
