# 1. Create a list of 6 numbers of your choice. Print the 2nd, last, and last-but-one element using indexing.

numbers = [1, 5, 8, 9, 6, 3]
print(numbers[1])
print(numbers[-1])
print(numbers[-2])

# Using slicing, print only the first 3 elements, then only the last 3 elements, 
# then the list reversed

numbers1 = [1, 4, 7, 9, 5, 3, 8]
print(numbers1[:3])
print(numbers1[-3:])
print(numbers1[::-1])

# Write a function find_max(numbers_list) that returns the largest number 
# WITHOUT using max() (loop through manually, track the largest seen so far)

def find_max(num):
    largest_num = num[0]
    for i in num:
        if i > largest_num:
            largest_num = i
    return largest_num
result = find_max([1, 4, 6, 9, 3, 6])
print(result)
print(find_max([100, 2, 55, 8]))

# Write a function remove_duplicates(numbers_list) that returns a new list with duplicates removed,
# preserving original order (don't use set() yet — loop and check manually)

def remove_duplicates(numbers_list):
    new_list = []
    for i in numbers_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
result1 = remove_duplicates([1, 4, 7, 8, 7, 1, 8])
print(result1)

# Take a list of numbers. Sort it in ascending order, then print it. 
# Then print it sorted in descending order WITHOUT modifying the original sort call
# (hint: think about sort() vs sorted())

numb = [1,5,7,4,3,5,6,7]
numb.sort()
print(numb)
print(sorted(numb,reverse=True))
print(numb)