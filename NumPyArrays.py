
import numpy as np

my_list = [1,2,3]
arr = np.array(my_list)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]
arrTwo = np.array(my_mat)

arrange = np.arange(0,20,2)
#// the last number is how much you want to count up by.



counting_numbers = np.linspace(0,50,10)
# works from the first number to the second with counts by the number of the last.


one_digit_arrays = np.ones(6)
# print 1 six times.

one_digit_double_arrays = np.ones((4,4))
#Double array of 1s 4x4

identity_matrix = np.eye(4)
# identity matrix is a matrix useful with linear algebra, two dimensional, diagnal of ones. 


random_array = np.random.rand(5)
#random numbers from 0 to 1

random_array_tuple = np.random.rand(5,5)
#random numbers from 0 to 1 in a multidemnsional array

random_array_int = np.random.randint(1,100,10)
#random numbers from 0 to 100, last number is how many numbers you want.


new_array = np.arange(25)

ranrarr = np.random.randint(0,50,10)

reshaped_array = new_array.reshape(5,5)
#changes the shape of an array. 


max = ranrarr.max()
#max value of an array

min = ranrarr.min()
#min value of an array


max_position = ranrarr.argmax()
#position of the highest number in the array

min_position = ranrarr.argmin()
#position of the lowest number in the array


print(my_list)
print(arr)
print(my_mat)
print(arrTwo)
print(arrange)
print(counting_numbers)
print(one_digit_arrays)
print(one_digit_double_arrays)
print(identity_matrix)
print(random_array)
print(random_array_tuple)
print(random_array_int)
print("--------------------------")
print(new_array)
print(ranrarr)
print(reshaped_array)
print("--------------------------")
print(max)
print(max_position)
print(min)
print(min_position)
print(ranrarr.shape)
print("--------------------------")
print("--------------------------")
print("--------------------------")
print("--------------------------")
print("----------ARRAY INDEXING----------------")

array_indexed = np.arange(0,11)
print(array_indexed[9])
print(array_indexed[1:4])

array_indexed[0:5] = 100
print(array_indexed)
#Changes the first 5 numbers to 100

two_dimen_array = np.array([[5,10,15], [20, 25, 30],[35,40,45],[50,55,60]])
print(two_dimen_array)
print(two_dimen_array[0,0])
print(two_dimen_array[0])
print(two_dimen_array[1,2])


print(two_dimen_array[:2,1:])
# to access the top right of the 2d Array you can use the above. It grabs everything up to row 2 and column 1 onwards
print(two_dimen_array[2:,1:])

conditional_selections = np.arange(1,11)
bool_array = conditional_selections > 5
print(bool_array)
print(conditional_selections[bool_array])
print(conditional_selections[conditional_selections>5])

test_array = np.arange(50).reshape(5,10)
print(test_array)
print(test_array[1:3,3:5])

print("--------------------------")
print("--------------------------")
print("--------------------------")
print("--------------------------")
print("----------ARRAY OPERATIONS----------------")

operation_array = np.arange(0,11)
print(operation_array)
add_array = operation_array + operation_array
minus_array = operation_array - operation_array
times_array = operation_array * operation_array
print(add_array)
print(minus_array)
print(times_array)

#You can also add to every element in the array e.g. operations_array + 100 will add 100 to every number

print("--------------------------")
print("--------------------------")
print("--------------------------")
print("--------------------------")
print("----------Test Exercises----------------")

array_zero = np.zeros(10)
print(array_zero)

array_ones = np.ones(10)
print(array_ones)

array_fives = np.full(10,5)
print(array_fives)

array_ints = np.arange(10,51)
print(array_ints)

array_ints_even = np.arange(10,50,2)
print(array_ints_even)

array_matrix = np.arange(9).reshape(3,3)
print(array_matrix)

identity_matrix_ones = np.eye(3)
print(identity_matrix_ones)

random_array_generated = np.random.randn(25)
print(random_array_generated)

random_array_matrix = np.linspace(0.01,1,100).reshape(10,10)
print(random_array_matrix)

array_linear = np.linspace(0,1,20)
print(array_linear)

print("--------------------------")

mat = np.arange(1,26).reshape(5,5)
print(mat)

print(mat[2:,1:])
print(mat[3:4,4:5])
print(mat[:3,1:2])
print(mat[4:,0:])
print(mat[3:,0:])

total_sum = np.sum(mat)
print(total_sum)

total_deviation = np.std(mat)
print(total_deviation)

total_sum_column = mat.sum(axis=0)
print(total_sum_column)