# main.py
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from legitarsasag import LegiTarsasag

def main():
    lt = LegiTarsasag("SkyLines")

    # Előre betöltött járatok
    lt.jarat_hozzaad(BelfoldiJarat("B101", "Debrecen", 12000))
    lt.jarat_hozzaad(NemzetkoziJarat("N202", "London", 50000))
    lt.jarat_hozzaad(NemzetkoziJarat("N203", "Berlin", 45000))

    # Előre betöltött foglalások
    lt.foglalas_letrehoz("Kiss Anna", "B101")
    lt.foglalas_letrehoz("Nagy Péter", "N202")
    lt.foglalas_letrehoz("Szabó Ákos", "N202")
    lt.foglalas_letrehoz("Fekete Júlia", "B101")
    lt.foglalas_letrehoz("Tóth Gábor", "N203")
    lt.foglalas_letrehoz("Kovács Lili", "N203")

    while True:
        print("\n=== Repülőjegy Foglalási Rendszer ===")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy opciót: ")

        if valasztas == "1":
            lt.listaz_jaratok()  # 🔍 új: járatok listázása foglalás előtt
            nev = input("Utas neve: ")
            jaratszam = input("Járatszám: ")
            lt.foglalas_letrehoz(nev, jaratszam)
        elif valasztas == "2":
            try:
                foglalas_id = int(input("Foglalás ID: "))
                lt.foglalas_lemondas(foglalas_id)
            except ValueError:
                print("❌ Érvénytelen ID.")
        elif valasztas == "3":
            lt.listaz_foglalasok()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("❌ Érvénytelen opció.")

if __name__ == "__main__":
    main()
