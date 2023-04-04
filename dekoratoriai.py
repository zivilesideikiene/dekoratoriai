# def returns_string(some_string):
#     return some_string
#
# def returns_upper_string(text, func):
#     if type(text) != str:
#         return 'input must be a type of string'
#     some_text = func(text)
#     return some_text.upper()
#
# print(returns_upper_string('higher order functions!', returns_string))


# 1 uzduotis: Parašykite dekoratorių kuris riboja parametrų kiekį (tarkime, ne daugiau negu
# 2 parametrai funkcijai).
#
# def args_suskaiciuoja(func):
#     def wrapper(*args, **kwargs):
#         if len(args) > 2:
#             return 'per daug argumentu'
#         return func(*args, **kwargs)
#     return wrapper
#
# print(args_suskaiciuoja("dekoratorius"))

# 1.2 Parašykite dekoratorių, kuris atideda funkcijos vykdymą 3s++++

# from time import sleep
#
# def uzvelavimas(laikas):
#     def uzvelavimas(fn):
#         def wrapper(*args, **kwargs):
#             sleep(laikas)
#             print(f"Funkcija buvo atidėta {laikas} sekundę(-es)")
#             return fn(*args, **kwargs)
#         return wrapper
#     return uzvelavimas
#
# def args_counter(fn):
#     def wrapper(*args, **kwargs):
#         print("Args number:", len(args))
#         return fn(*args, **kwargs)
#     return wrapper
#
# @uzvelavimas(3)
# @args_counter
# def sumavimas(*args):
#     print("Skaičių suma:", sum(args))
#
# sumavimas(50, 30, 20, 15)

# 2 uzduotis: Parašykite dekoratorių, kuris leidžia į funkciją įrašyti tik string tipo parametrus.

# def string_args_only(fn):
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if type(i) != str:
#                 return "Tai nera stringas!"
#         return fn(*args, **kwargs)
#     return wrapper
#
# @string_args_only
# def fn(s):
#     return "Labas " + s
#
# wrapped_fn = string_args_only(fn)
#
# print(wrapped_fn("pasauli tu esi nuostabus"))



# 3 uzduotis: Turime tokį kodą:
import requests  # importuojame requests
from time import time  # importuojame time modulį
from functools import wraps

def speed_test(fn):
    wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        fn(*args, **kwargs)
        end_time = time()
        runtime = end_time - start_time
        print(f"Function's '{fn.__name__}', with given parameters {args} runtime: {round(runtime, 2)}s")
    return wrapper


@speed_test
def get_status(website):
    r = requests.get(website)
    print(r.status_code)


get_status('http://python.org')

@speed_test
def prime_finder(given_range):
    final_list = []
    for num in range(given_range):
        if num > 1:
            for i in range(2,num):
                    if (num % i) == 0:
                        break
            else:
                final_list.append(num)
    return final_list

prime_finder(10000)


start_time = time()  # fiksuojame starto laiką
r = requests.get('http://www.cnn.com')  # sukuriame http užklausą
print(r.status_code)  # spausdiname status code (200 = OK, 404 = Not Found, ir
# t.t. galima pasiguglinti http status codes)
end_time = time()  # fiksuojame pabaigos laiką
print(end_time - start_time)  # atspausdiname laiką, per kurį gaovme atsakymą
# #
# Parašykite dekoratorių, bet kokios funkcijos vykdymo laikui fiksuoti.
# Galite patobulinti, pvz funkcijos (vardas), su tokiais ir tokiais argumentais vykdymo
# laikas - XX s. Ištestuokite, su funkcija, grąžinančia svetainės atsako kodą ir su funkcija,
# išrenkančia pirminius skaičius užduotame diapazone.


