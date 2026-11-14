
import tkinter as tk
from tkinter import messagebox
import csv
import os
import json
import sqlite3
import random
import requests
from datetime import datetime
from kocka_dobas import KockaDobas


class KockaApp(KockaDobas):

    def __init__(self, root):
        super().__init__()

        self.root = root
        self.root.title("Kockadobó alkalmazás")
        self.root.geometry("380x650")

        self.adatbazis_letrehozas()

        self.cimke = tk.Label(
            root,
            text="Add meg a dobások számát:"
        )
        self.cimke.pack(pady=10)

        self.bevitel = tk.Entry(root)
        self.bevitel.pack(pady=5)

        self.gomb = tk.Button(
            root,
            text="Dobás",
            command=self.dobas_indit
        )
        self.gomb.pack(pady=10)
        self.veletlen_gomb = tk.Button(
            root,
            text="Véletlen dobásszám",
            command=self.veletlen_darabszam
        )
        self.veletlen_gomb.pack(pady=5)

        self.eredmeny = tk.Label(
            root,
            text="Az eredmények itt jelennek meg"
        )
        self.eredmeny.pack(pady=10)

        self.mentes_txt_gomb = tk.Button(
            root,
            text="Mentés TXT-be",
            command=self.mentes_txt
        )
        self.mentes_txt_gomb.pack(pady=5)

        self.mentes_csv_gomb = tk.Button(
            root,
            text="Mentés CSV-be",
            command=self.mentes_csv
        )
        self.mentes_csv_gomb.pack(pady=5)

        self.mentes_json_gomb = tk.Button(
            root,
            text="Mentés JSON-ba",
            command=self.mentes_json
        )
        self.mentes_json_gomb.pack(pady=5)

        self.mentes_sql_gomb = tk.Button(
            root,
            text="Mentés adatbázisba",
            command=self.mentes_sql
        )
        self.mentes_sql_gomb.pack(pady=5)

        self.torles_gomb = tk.Button(
            root,
            text="Adatbázis ürítése",
            command=self.adatbazis_urites
        )
        self.torles_gomb.pack(pady=5)

        self.statisztika = tk.Label(
            root,
            text="Adatbázis statisztika"
        )
        self.statisztika.pack(pady=10)

        self.backend_gomb = tk.Button(
            root,
            text="Kapcsolat a backenddel",
            command=self.backend_kapcsolat
        )
        self.backend_gomb.pack(pady=5)

        self.statisztika_frissites()

        self.kilepes = tk.Button(
            root,
            text="Kilépés",
            command=root.destroy
        )
        self.kilepes.pack(pady=15)

    def dobas_indit(self):
        try:
            darab = int(self.bevitel.get())

            if darab < 1 or darab > 10000:
                raise ValueError

            eredmenyek = self.dobas(darab)

            szoveg = f"Összes dobás: {darab}\n\n"

            for szam, mennyiseg in eredmenyek.items():
                szoveg += f"{szam}: {mennyiseg} alkalommal\n"

            self.eredmeny.config(text=szoveg)

        except ValueError:
            messagebox.showerror(
                "Hiba",
                "1 és 10000 közötti egész számot adj meg!"
            )

    def mentes_txt(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning(
                "Figyelmeztetés",
                "Először végezz el egy dobást!"
            )
            return

        try:
            with open(
                "mentes.txt",
                "a",
                encoding="utf-8"
            ) as fajl:

                fajl.write("Kockadobás eredményei:\n")

                for szam, mennyiseg in self.eredmenyek.items():
                    fajl.write(
                        f"{szam}: {mennyiseg} alkalommal\n"
                    )

                fajl.write("\n")

            messagebox.showinfo(
                "Mentés",
                "Az eredmények sikeresen mentve TXT-be!"
            )

        except OSError:
            messagebox.showerror(
                "Hiba",
                "Nem sikerült menteni a TXT-fájlt!"
            )

    def mentes_csv(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning(
                "Figyelmeztetés",
                "Először végezz el egy dobást!"
            )
            return

        try:
            fajlnev = "mentes.csv"

            fejlec_kell = (
                not os.path.exists(fajlnev)
                or os.path.getsize(fajlnev) == 0
            )

            adatok = self.eredmenyek.copy()
            adatok["Dátum"] = datetime.now().strftime(
                "%Y.%m.%d %H:%M:%S"
            )

            with open(
                fajlnev,
                "a",
                newline="",
                encoding="utf-8"
            ) as fajl:

                iro = csv.writer(fajl)

                if fejlec_kell:
                    iro.writerow(adatok.keys())

                iro.writerow(adatok.values())

            messagebox.showinfo(
                "Mentés",
                "Az eredmények sikeresen mentve CSV-be!"
            )

        except OSError:
            messagebox.showerror(
                "Hiba",
                "Nem sikerült menteni a CSV-fájlt!"
            )

    def mentes_json(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning(
                "Figyelmeztetés",
                "Először végezz el egy dobást!"
            )
            return

        try:
            with open(
                "mentes.json",
                "r",
                encoding="utf-8"
            ) as fajl:

                adatok = json.load(fajl)

        except FileNotFoundError:
            adatok = []

        except json.JSONDecodeError:
            messagebox.showerror(
                "Hiba",
                "A JSON-fájl tartalma hibás!"
            )
            return

        try:
            uj_adat = self.eredmenyek.copy()

            uj_adat["Dátum"] = datetime.now().strftime(
                "%Y.%m.%d %H:%M:%S"
            )

            adatok.append(uj_adat)

            with open(
                "mentes.json",
                "w",
                encoding="utf-8"
            ) as fajl:

                json.dump(
                    adatok,
                    fajl,
                    indent=4,
                    ensure_ascii=False
                )

            messagebox.showinfo(
                "Mentés",
                "Az eredmények sikeresen mentve JSON-ba!"
            )

        except OSError:
            messagebox.showerror(
                "Hiba",
                "Nem sikerült menteni a JSON-fájlt!"
            )

    def adatbazis_letrehozas(self):
        try:
            kapcsolat = sqlite3.connect("kockadobas.db")
            kurzor = kapcsolat.cursor()

            kurzor.execute("""
                CREATE TABLE IF NOT EXISTS dobasok (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    datum TEXT,
                    oldal1 INTEGER,
                    oldal2 INTEGER,
                    oldal3 INTEGER,
                    oldal4 INTEGER,
                    oldal5 INTEGER,
                    oldal6 INTEGER
                )
            """)

            kapcsolat.commit()
            kapcsolat.close()

        except sqlite3.Error as hiba:
            messagebox.showerror(
                "Adatbázishiba",
                str(hiba)
            )

    def mentes_sql(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning(
                "Figyelmeztetés",
                "Először végezz el egy dobást!"
            )
            return

        try:
            kapcsolat = sqlite3.connect("kockadobas.db")
            kurzor = kapcsolat.cursor()

            datum = datetime.now().strftime(
                "%Y.%m.%d %H:%M:%S"
            )

            kurzor.execute("""
                INSERT INTO dobasok
                (datum, oldal1, oldal2, oldal3,
                 oldal4, oldal5, oldal6)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                datum,
                self.eredmenyek[1],
                self.eredmenyek[2],
                self.eredmenyek[3],
                self.eredmenyek[4],
                self.eredmenyek[5],
                self.eredmenyek[6]
            ))

            kapcsolat.commit()
            kapcsolat.close()

            self.statisztika_frissites()

            messagebox.showinfo(
                "Mentés",
                "Az eredmények sikeresen mentve az adatbázisba!"
            )

        except sqlite3.Error as hiba:
            messagebox.showerror(
                "Adatbázishiba",
                str(hiba)
            )

    def statisztika_frissites(self):
        try:
            kapcsolat = sqlite3.connect("kockadobas.db")
            kurzor = kapcsolat.cursor()

            kurzor.execute("""
                SELECT
                    SUM(oldal1),
                    SUM(oldal2),
                    SUM(oldal3),
                    SUM(oldal4),
                    SUM(oldal5),
                    SUM(oldal6)
                FROM dobasok
            """)

            eredmeny = kurzor.fetchone()

            kapcsolat.close()

            szoveg = "Összesített dobások:\n\n"

            for i in range(6):
                mennyiseg = eredmeny[i]

                if mennyiseg is None:
                    mennyiseg = 0

                szoveg += f"{i + 1}: {mennyiseg} alkalommal\n"

            self.statisztika.config(text=szoveg)

        except sqlite3.Error as hiba:
            messagebox.showerror(
                "Adatbázishiba",
                str(hiba)
            )

    def adatbazis_urites(self):
        valasz = messagebox.askyesno(
            "Megerősítés",
            "Biztosan törölni szeretnéd az összes adatbázis-rekordot?"
        )

        if valasz:
            try:
                kapcsolat = sqlite3.connect("kockadobas.db")
                kurzor = kapcsolat.cursor()

                kurzor.execute("DELETE FROM dobasok")

                kapcsolat.commit()
                kapcsolat.close()

                self.statisztika_frissites()

                messagebox.showinfo(
                    "Törlés",
                    "Az adatbázis sikeresen kiürítve!"
                )

            except sqlite3.Error as hiba:
                messagebox.showerror(
                    "Adatbázishiba",
                    str(hiba)
                )

    def veletlen_darabszam(self):
        darab = random.randint(10, 500)

        self.bevitel.delete(0, tk.END)
        self.bevitel.insert(0, str(darab))

    def backend_kapcsolat(self):
        try:
            valasz = requests.get(
                "http://127.0.0.1:5000/api/uzenet"
            )

            adatok = valasz.json()

            messagebox.showinfo(
                "Backend üzenet",
                adatok["message"]
            )

        except requests.exceptions.ConnectionError:
            messagebox.showerror(
                "Kapcsolódási hiba",
                "Nem sikerült kapcsolódni a backend szerverhez!"
            )
