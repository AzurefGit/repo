# f = open('tekst1.txt', 'r+', encoding="UTF-8")
# s= f.read()
# breakpoint()
# print(s)
# print(type(s))

# --------------------

import numpy as np
import pandas as pd
# Dane z pliku CSV (przykładowe dane)
# Zakładam, że masz już wczytane dane do tablicy 'data'
data = np.genfromtxt('jajka2024.csv', delimiter=";", dtype=('|U16'), encoding="UTF-8")


# Wyodrębnij ceny jaj (zakładam, że druga kolumna zawiera ceny jaj)
ceny_jaj = data[1:,1]  # Zakładam, że druga kolumna zawiera ceny jaj
c_data= [x for x in ceny_jaj if x!='']

# Konwertuj ceny jaj na liczby zmiennoprzecinkowe
ceny_jaj_float = np.array([float(cena.replace(',', '.')) for cena in c_data])

# # Oblicz średnią cenę jaj
srednia_cena_jaj = np.mean(ceny_jaj_float)

print(f"Średnia cena jaj wynosi: {srednia_cena_jaj:.2f} zł")