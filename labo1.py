#1A
#typ wyniku działania: 1+2
from encodings.idna import ace_prefix
from tkinter import XView
from xml.sax.handler import property_interning_dict

x =1+2
print(type(x))
#<class 'int'>

#typ wyniku działania: 1+45
x =1+4.5
print(type(x))
#<class 'float'>

#typ wyniku działania: 3/2
x =3/2
print(type(x))
#<class 'float'>

#typ wyniku działania:  4/2
x =4/2
print(type(x))
#<class 'float'>

#typ wyniku działania: 3//2
x =3//2
print(type(x))
#<class 'int'>


#typ wyniku działania: -3//2
x =-3//2
print(type(x))
#<class 'int'>

#typ wyniku działania: 11%2
x = 11%2
print(type(x))
#<class 'int'>

#typ wyniku działania; 2**10
x = 2**10
print(type(x))
#<class 'int'>


#typ wyniku działania: 8**(1/3)
x = 8**(1/3)
print(type(x))
#<class 'float'>

#1B
# 1. Konwersja float na int
print(int(3.0))  # Wynik: 3

# 2. Konwersja int na float
print(float(3))  # Wynik: 3.0

# 3. Konwersja string na float
print(float("3"))  # Wynik: 3.0

# 4. Konwersja float na string
print(str(12.4))  # Wynik: '12.4'

# 5. Konwersja 0 na wartość logiczną
print(bool(0))  # Wynik: False


#2

uczelnia = "Studiuję na WSIiZ"
print(uczelnia)

#3
imie='Jan'
wiek=20
wzrost=178
print(f"Nazywam się {imie} i mam {wiek} lat.")
print(f"Moj wzrost to {wzrost}")

#4
Cena=39.99
Rabat=0.2
#obliczenie ceny po rabacie
Cena_po_rabacie = Cena * (1 - Rabat)
print(f"Cena po rabacie wynosi: {Cena_po_rabacie:.2f} PLN")

#5
bok_a = float(input("Podaj długość boku a= "))
bok_b = float(input("Podaj długość boku b= "))

#obliczenie obwodu i pola prostokąta
obwód = 2*(bok_a+bok_b)
pole = bok_a*bok_b

print(f"pole prostokąta wynosi {pole:.2f}")
print(f"obwód prostokąta wynosi {obwód:2f}")

#6
#Skrypt pobierający od użytkownika dane i obliczający zużycie paliw oraz koszt podróży
droga=float(input("podaj droge przebytą przez samochód(w km):"))
spalanie=float(input("podaj srednie spalanie samochodu(w litrach na 100km):"))

# Stała cena paliwa
cena_paliwa = 6.5

# Obliczenia
zuzycie_paliwa = (droga / 100) * spalanie
koszt_podrozy = zuzycie_paliwa * cena_paliwa

# Wynik
print(f"Zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Koszt podróży: {koszt_podrozy:.2f} zł")

#A
import random
#generowanie losowej drogi
droga = random.randint(1, 10**9)
spalanie = float(input("podaj srednie spalanie samochodu (w litrach na 100km"))
cena_paliwa = float(input("podaj cene paliwa(w PLN)"))

#Obliczenia
zuzycie_paliwa = ((droga/100)*spalanie)
koszt_podrozy =zuzycie_paliwa * cena_paliwa

#wyniki
print(f"losowa dlugosc")
# losowanie z zakresu od 1 do 1 miliarda

print(f"losowa długośc drogi:{droga}km")
print (f"aktualna cena paliwa:{cena_paliwa:.2f}PLN")
print(f"zużycie paliwa:{zuzycie_paliwa:.2f}litrów")

#B
import random

# Generowanie losowej drogi
droga = random.randint(1, 1000)  # losowa droga w km z zakresu od 1 do 1000 km
spalanie = float(input("Podaj średnie spalanie samochodu (w litrach na 100 km): "))
cena_paliwa = float(input("Podaj cenę paliwa za litr: "))

# Obliczenia
zuzycie_paliwa = (droga / 100) * spalanie
koszt_podrozy = zuzycie_paliwa * cena_paliwa

# Wynik z f-stringiem
print(f"Losowa długość przejechanej drogi: {droga} km")
print(f"Średnie spalanie: {spalanie:.2f} l/100 km")
print(f"Zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Koszt podróży przy cenie {cena_paliwa:.2f} zł/l: {koszt_podrozy:.2f} zł")

#7
#Równanie ax+b=0
#pobieranie wartosci od użytkownika

a=float(input("podaj a="))
b=float(input("podaj b="))

# Rozwiązywanie równania
if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań.")
    else:
        print("Równanie nie ma rozwiązań.")
else:
    x = -b / a
    print(f"Rozwiązanie równania: x = {x}")
#8
#Równanie ax2 + bx + c = 0
#Pobieramy dane od użytkownika

a=float(input("podaj a="))
b=float(input("podaj b="))
c=float(input("podaj c="))

#sprawdzenie czy jest to rownanie kwadratowe
if a==0:
    print(f"to nie jest rownianie kwadratowe")

#Rozwiązanie równania
delta = b**2 - 4 * a * c

#Wyswietlanie delty
print(f"delta:{delta}")

#Rowzwiązanie w zależności od wyniku delty
if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"rownanie ma dwa rozwiazania x1={x1:.2f} x2={x2:.2f}")

elif delta == 0:
    x = (-b/2*a)
    print(f"rownanie ma jedno rozwiązanie x={x:.2f}")

else:
    print(f"nie ma rozwiązania")

#8

# Pobranie dwóch liczb od użytkownika
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

# Obliczenia
dodawanie = liczba1 + liczba2
odejmowanie = liczba1 - liczba2
mnożenie = liczba1 * liczba2
dzielenie = liczba1 / liczba2 if liczba2 != 0 else "Dzielenie przez zero jest niemożliwe"
potegowanie = liczba1 ** liczba2

# Wyświetlanie wyników
print(f"Dodawanie: {liczba1} + {liczba2} = {dodawanie}")
print(f"Odejmowanie: {liczba1} - {liczba2} = {odejmowanie}")
print(f"Mnożenie: {liczba1} * {liczba2} = {mnożenie}")
print(f"Dzielenie: {liczba1} / {liczba2} = {dzielenie}")
print(f"Potęgowanie: {liczba1} ** {liczba2} = {potegowanie}")
