from functools import reduce


def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1,2,3,4,5])
print(result)

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))

#Decorators
# def greeting():
#     return 'Welcome to Python'
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# g = uppercase_decorator(greeting)
# print(g())

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to teach.")

print_full_name("Michał", "Gnaciński", "Polska")

numbers = [1,2,3,4,5]
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))
numbers_squared2 = map(lambda x : x ** 2, numbers)
print(list(numbers_squared2))

numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int,numbers_str)
print(list(numbers_int))

names = ['Anna', "Jan", "Michal", "Martyna"]
def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))
names_upper_cased2 = map(lambda name: name.upper(), names)
print(list(names_upper_cased2))

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

def is_name_long(name):
    if len(name) > 5:
        return True
    return False

odd_long_names = filter(is_name_long, names)
print(list(odd_long_names))

def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums,numbers_str)
print(total)


#Exercise
countries_ex = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names_ex = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers_ex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
country_to_upper = map(lambda coun: coun.upper(), countries_ex)
print(list(country_to_upper))

#2
numbers_squared = map(lambda x: x**2, numbers_ex)
print(list(numbers_squared))

#3
names_to_upper = map(lambda nm: nm.upper(), names_ex)
print(list(names_to_upper))

#4
def contains_land(country):
    if "onia" in country:
        return True
    return False
country_contains_land = filter(contains_land, countries_ex)
print(list(country_contains_land))

#5
def six_char(country):
    if len(country) == 6:
        return True
    return False
country_six_char = filter(six_char, countries_ex)
print(list(country_six_char))

#6
def six_or_more(country):
    if len(country) >= 6:
        return True
    return False
country_six_or_more = filter(six_or_more, countries_ex)
print(list(country_six_or_more))

#7 
def starts_with_e(country):
    if country.startswith("E"):
        return True
    return False
country_starts_with_e = filter(starts_with_e, countries_ex)
print(list(country_starts_with_e))

#8
chained = filter(
    contains_land,
    filter(
        six_or_more,
        countries_ex
    )
)
print(list(chained))