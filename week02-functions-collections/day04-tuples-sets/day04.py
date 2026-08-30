# 1. Create a tuple with your name, age, and city. Unpack it into 3 separate variables and print each.

profile = ("Pinank", 33, "Mumbai")
name, age, city = profile
print(name)
print(age)
print(city)

# Write a function get_min_max(numbers_list) that returns BOTH the min and max
# as a tuple, WITHOUT using min()/max() (reuse your manual find_max logic from 
# yesterday, plus a similar find_min approach)

def get_min_max(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    for i in numbers:
        if i < min_num:
            min_num = i
    return min_num, max_num
result = get_min_max([1, 4, 7, 3, 6, 8, 2])
print(result)

# Using sets, find:
# 1. students in BOTH classes
# 2. students ONLY in class_a
# 3. students in EITHER class (combined, no duplicates)


class_a = {"Amit", "Priya", "Rahul", "Sara"}
class_b = {"Priya", "John", "Sara", "Mike"}

print("In both classes:", class_a & class_b)
print("Only in class_a:", class_a - class_b)
print("In either class:", class_a | class_b)

# Take a list with duplicate numbers. Remove duplicates using set(), 
# then convert back to a list. Compare this one-liner to your Day 3 remove_duplicates() function.

numbers1 = [1, 5, 7, 9, 5, 7, 3, 3, 4]
no_duplicate = list(set(numbers1))
print(no_duplicate)

# Day 3 remove_duplicates(): preserves original order, but requires a manual loop (more code)
# Day 4 list(set(numbers)): much shorter (1 line), but does NOT guarantee original order is preserved
# → use the set version when order doesn't matter; use the manual loop version when it does