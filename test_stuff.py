import math

# this is O(n^2) runtime
def square(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
#print(square(4))



# this is O(log n) runtime, recursive example
def log_func(n):
    if n == 0:
        return "done"
    n = n // 2
    return log_func(n)
#print(log_func(8))


# O(log n) iterative/non-recursive example
def log_n(n):
    while n > 1:
        n = n // 2
    print(n)
#log_n(8)


# Binary Search O(log n) runtime
# in order for binary search to work the array must be an ordered array
# array = []
# first_index = 0
# target_search = 666
# appending numbers from 1 to 1024 to array
# for i in range(1, 1025):
#     array.append(i)
#print(array)
# last_index = len(array) - 1

# def binary_search(array, first_index, last_index, target_search):
#     if first_index > last_index:
#         return False
    
#     mid_ind = (first_index + last_index) // 2

#     if array[mid_ind] == target_search:
#         return True
#     elif array[mid_ind] > target_search:
#         return binary_search(array, first_index, mid_ind - 1, target_search)
#     elif array[mid_ind] < target_search:
#         return binary_search(array, mid_ind + 1, last_index, target_search)
#print(binary_search(array, first_index, last_index, target_search))





# this is O(n log n) runtime
def nLogNfunction(n):
    y = n

    while n > 1:
        n = n // 2
        for i in range(y):
            print(i)
#nLogNfunction(4)





# this is a merge sort function runtime of O(n log n)
def merge_sort(arr):  # this is O(log n)
    if len(arr) < 2:
        return arr
    
    mid_index = len(arr) // 2
    left_arr = arr[:mid_index]
    right_arr = arr[mid_index:]

    def merge(left_arr, right_arr):
        result_arr = []
        left_index = 0
        right_index = 0

        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] < right_arr[right_index]:
                result_arr.append(left_arr[left_index])
                left_index += 1
            else:
                result_arr.append(right_arr[right_index])
                right_index += 1
        return result_arr + left_arr[left_index:] + right_arr[right_index:]

    return merge(merge_sort(left_arr), merge_sort(right_arr)) # this line of code is O(n)
# therefore the whole function is O (n log n) because O(log n) * O(n) = O(n log n)
array = [12,3,16,6,5,1]
sorted_array = merge_sort(array)
# print(sorted_array)








# this is O(2^n) runtime with fibonacci
def fib(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    
    return fib(n - 1) + fib(n - 2) 
#print(fib(4))






# this is O(n!) runtime
def f(n):
    if n == 0:
        print("***************")
        return
    
    for i in range(n):
        f(n - 1)
f(3)

