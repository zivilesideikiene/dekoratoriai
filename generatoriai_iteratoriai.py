# def skaiciuojam_iki(iki):
#     count = 1
#     while count <= iki:
#         yield count
#         count +=1


# 1 uzduotis: Parašykite generatorių, kuris kaskartą inicijuotas su funkcija next grąžintų
# sekantį porinį skaičių. Pirmas sk. 2, toliau 4 ir taip be pabaigos.

# def poriniai():
#     number = 2
#     while True:
#         yield number
#         number += 2
#
# generator = poriniai()
# for i in range(9):
#     print(next(generator))


# 2 uzduotis: Parašykite generatorių , kuris kas kartą generuotų po vieną Fibonačio sekos skaičių.
# (Seka prasideda šiais skaičiais: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233. Kiekvienas
# šios sekos skaičius lygus dviejų prieš jį einančių skaičių sumai, daugiau google:
# def fibonacio_seka():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib = fibonacio_seka() #generatorius
# for i in range(10):
#     print(next(fib))


# 3 uzduotis: Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą. Parašykite generatorių,
# kuris tikrins po viena kombinaciją, pradedant 0000, ir sustos, kai pin kodas bus teisingas.
# Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau. Pabaigus funkciją, praiteruokite
# sukurtą generatorių su for ciklu, kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį,
# parašytų 'PIN is XXXX(jųsų pin'as)'. Atkreipkite dėmesį, kad kodas gali prasidėti nuliu.
#  Sugalvokite, kaip apeiti šią problemą :).

# PIN = '0549'  #blogas?
# def skaiciuojam_iki(pin):
#     for i in range(10000):
#         kodas = '{:04}'.format(i) #padarau, kad butu 4 skaiciai
#         if kodas == pin:
#             yield f'PIN yra {pin}'
#             return
#         else:
#             yield kodas
#
# sk = skaiciuojam_iki(PIN) #generatorius
#
# for kodas in sk:
#     print(kodas)

# arba
#
# PIN = '0012'
#
# def pin_breaker():
#     num = 0
#     while num < 10000:
#         guess = f'{num:04}'
#         if guess == PIN:
#             print(f"{guess} That's your PIN!")
#             break
#         yield guess
#         num += 1
#
# gen = pin_breaker()
#
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break

# 4 uzduotis: Parašykite generatoriaus funkciją, kuri atidarytų nurodytą tekstinį failą, ir grąžintų
# po vieną eilutę (tiesiog yield'inti reikės ne skaičių o kitą duomenų tipą.). Reikės prisiminti darbą
# su failais :)
import os

# os.chdir("C:\Users\Zivile\PycharmProjects\dekoratoriai1") #dabar esu

# with open('tekstas1.txt', 'w') as failas:  #sukuria faila .txt
#     failas.write()

with open('tekstas.txt', 'r') as failas:  #atspausdina teksta
    failas.read()

# def read_lines(filename):#blogas
#     with open(filename, 'r') as file:
#         for line in file:
#             yield line.strip()
#
# for line in read_lines('tekstas.txt'):
#     print(line)

# # arba
# def read_in_lines(filename):
#     with open(filename, 'r', encoding="utf-8") as file:
#         for line in file:
#             yield line[:-1]
#
#
# generator = read_in_lines('tekstas.txt')
#
# for x in generator:
#     print(x)

