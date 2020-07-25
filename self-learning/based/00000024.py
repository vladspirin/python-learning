import copy


# def my_copy(obj, copy_mode):
#     return copy.deepcopy(obj) if copy_mode == "deep copy" else copy.copy(obj)

# obj = [[1, 2], [3, 4]]
# def detect_copy():
#     copy_obj = copying_machine(obj)
#     if copy_obj == copy.copy((copy_obj)):
#         return 'shallow copy'
#     if copy_obj == copy.deepcopy(copy_obj):
#         return 'deep copy'

# print(detect_copy())



# sorting function
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


# where copying takes place
arr = [int(i) for i in input().split()]
print(arr)
sorted_arr = copy.copy(bubble_sort(arr))
print(sorted_arr)
# all(print('sorted') if i != j else print('not sorted') for i, j in zip(arr, sorted_arr))
lst = []
for i, j in zip(arr, sorted_arr):
    lst.append(id(i, j))
print(lst)

