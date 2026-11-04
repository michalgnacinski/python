import numpy as np

python_list = [1,2,3,4,5]
print('Type: ', type(python_list))
print(python_list)

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
print(numpy_array_from_list)
numpy_float_array = np.array(python_list, dtype=float)
print(numpy_float_array)
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) 

numpy_two_dimensional_list = np.array(two_dimensional_list)
print(numpy_two_dimensional_list)

print('two dimensial array: ', numpy_two_dimensional_list.tolist())