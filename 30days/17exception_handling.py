try:
    name = input("Enter a your name: ")
    year_born = input("Enter your year of birth: ")
    age = 2026 - year_born
    print(f"Hello {name}, you are {age} years old.")
except Exception as e:
    print(f"Error: {e}")
# except TypeError: 
#     print("Type error occoured")
# except ValueError:
#     print("Value error occoured")
# except ZeroDivisionError:
#     print("Zero division error occoured")
# else:
#     print("No error occoured")
# finally:
#     print("I always run no matter what")

#Uppacking and Packing Arguments 
def sum_of_five_nums(a,b,c,d,e):
    return a+b+c+d+e
lst = [1,2,3,4,5]
print(sum_of_five_nums(*lst))

numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)
print(numbers)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin,sw, nor, *rest = countries
print(fin, sw, nor, rest)
numbers2 = [1,2,3,4,5,6,7]
one, *middle, last = numbers2
print(one, middle, last)

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in{country}, {city}, he is {age} year old'
dct = {'name':'Michal', 'country':'Poland', 'city':'Poznan', 'age':20}
print(unpacking_person_info(**dct))

def sum_all(*args):
    s = 0
    for i in args:
        s+=i
    return s
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6,7))

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Michał", country="Poland", city="Poznan", age=20))

#Spreading
lst_one = [1,2,3]
lst_two = [4,5,6,7]
lst = [0, *lst_one, *lst_two]
print(lst)
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

#Enumerate
for index, item in enumerate([20,30,40]):
    print(index, item)

for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

#Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f,v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

#Exercise 1
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries2, es, ru = names
print(nordic_countries2)
es_ru = f"{es}  {ru}"
print(es_ru)
print(ru)
