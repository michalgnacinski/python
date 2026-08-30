language = 'Python'
lst = list(language)
print(lst)

lst2 = [i for i in language]
print(lst)

numbers = [i for i in range(11) if i % 2 !=0]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers_tuple = [(i, i * i) for i in range(11)]
print(numbers_tuple)

even_numbers = [i for i in range (21) if i % 2 == 0]
print(even_numbers)



add_two_nums = lambda a, b: a + b
print(add_two_nums(2,4))

square = lambda x : x ** 2
print(square(3))

multiple_variables = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variables(5,5,3))

#Exercises

#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print_nums = [i for i in numbers if i <= 0]
print(print_nums)

#2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [i for row in list_of_lists for i in row]
print(flattened_list)

#3
for i in range(11):
    lista = [i*1*j for j in range(7)]
    print(lista)