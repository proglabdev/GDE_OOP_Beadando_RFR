# legitarsasag.py
from jegy_foglalas import JegyFoglalas

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaad(self, jarat):
        self.jaratok.append(jarat)

    def foglalas_letrehoz(self, utas_nev, jaratszam):
        jarat = next((j for j in self.jaratok if j.jaratszam == jaratszam), None)
        if not jarat:
            print("❌ Hiba: Nem létező járatszám.")
            return
        foglalas_id = len(self.foglalasok) + 1
        foglalas = JegyFoglalas(foglalas_id, utas_nev, jarat)
        self.foglalasok.append(foglalas)
        print(f"✅ Sikeres foglalás! Ár: {jarat.jegyar} Ft")

    def foglalas_lemondas(self, foglalas_id):
        for f in self.foglalasok:
            if f.foglalas_id == foglalas_id:
                self.foglalasok.remove(f)
                print("✅ Foglalás sikeresen törölve.")
                return
        print("❌ Hiba: Nincs ilyen foglalás.")

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("ℹ️ Nincsenek aktív foglalások.")
            return
        for f in self.foglalasok:
            print(f"#{f.foglalas_id} - {f.utas_nev} -> {f.jarat.celallomas} ({f.jarat.jarat_tipus()}, {f.jarat.jegyar} Ft)")

    def listaz_jaratok(self):
        if not self.jaratok:
            print("Nincsenek elérhető járatok.")
            return
        print("\n✈️ Elérhető járatok:")
        for jarat in self.jaratok:
            print(f"- {jarat.jaratszam}: {jarat.celallomas} ({jarat.jarat_tipus()}, {jarat.jegyar} Ft)")
