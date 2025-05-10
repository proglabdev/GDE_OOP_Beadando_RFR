# jegy_foglalas.py
from jarat import Jarat

class JegyFoglalas:
    def __init__(self, foglalas_id, utas_nev, jarat: Jarat):
        self.foglalas_id = foglalas_id
        self.utas_nev = utas_nev
        self.jarat = jarat
