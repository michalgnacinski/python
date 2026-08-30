list_org = ["banana", "apple", "cherry"]

list_copy = list_org.copy()

list_copy.append("lemon")
print(list_copy)
print(list_org)

a = [1,2,3,4,5,6]
b = [i*i for i in a]

print(a)
print(b)