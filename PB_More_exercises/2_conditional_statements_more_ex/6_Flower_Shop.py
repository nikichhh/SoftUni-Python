import math

magnolii = int(input())
zyumbyuli = int(input())
rozi = int(input())
kaktusi = int(input())
cena_na_podaruk = float(input())

suma = magnolii * 3.25 + zyumbyuli * 4 + rozi * 3.5 + kaktusi * 8
suma -= suma * 0.05

if cena_na_podaruk <= suma:
    print(f"She is left with {math.floor(suma - cena_na_podaruk)} leva.")
else:
    print(f"She will have to borrow {math.ceil(cena_na_podaruk - suma)} leva.")