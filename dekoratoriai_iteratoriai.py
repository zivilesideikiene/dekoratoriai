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






# 3 uzduotis: Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą. Parašykite generatorių,
# kuris tikrins po viena kombinaciją, pradedant 0000, ir sustos, kai pin kodas bus teisingas.
# Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau. Pabaigus funkciją, praiteruokite
# sukurtą generatorių su for ciklu, kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį,
# parašytų 'PIN is XXXX(jųsų pin'as)'. Atkreipkite dėmesį, kad kodas gali prasidėti nuliu.
#  Sugalvokite, kaip apeiti šią problemą :).





# 4 uzduotis: Parašykite generatoriaus funkciją, kuri atidarytų nurodytą tekstinį failą, ir grąžintų
# po vieną eilutę (tiesiog yield'inti reikės ne skaičių o kitą duomenų tipą.). Reikės prisiminti darbą
# su failais :)


