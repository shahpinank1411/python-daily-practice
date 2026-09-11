# A1. Write a function is_prime(n) (reuse your Day 1 corrected version, including the n < 2 guard clause). Then write a second function primes_in_range(start, end) that uses is_prime() to return a list of all prime numbers between start and end (inclusive). Test with primes_in_range(1, 30).
def is_prime(n):
    if n < 2:
        return False
    
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            return prime
    if prime:
        return True
def primes_in_range(a, b):
    primes = []
    for i in range(a, b+1):
        if is_prime(i):
            primes.append(i)
    return primes


result = primes_in_range(1, 30)
print(result)

# Write a function find_longest_word(sentence) that takes a sentence (string), 
# splits it into words, and returns the longest word — without using any 
# built-in max-finding shortcut (loop manually, same pattern as Day 3's find_max)

def find_longest_word(string):
    new_split = string.split()
    longest_word = new_split[0]
    for i in new_split:
        if len(i) > len(longest_word):
            longest_word = i
    return longest_word
     
    
result = find_longest_word("the quick brown fox jumping over the lazy dog the fox runs")
print(result)

# You're given: [12, 7, 18, 3, 25, 9, 30, 14]
# Using a single loop, build TWO separate lists: 
# one containing only even numbers, one containing only odd numbers. Print both.

numbers = [12, 7, 18, 3, 25, 9, 30, 14]
even = []
odd = []
for i in numbers:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)

print(f"even numbers are {even}")
print(f"odd numbers are {odd}")

# Write a function char_frequency(word) that returns a dictionary counting 
# how many times EACH character appears in the word. Test with char_frequency("mississippi")

def char_frequency(word):
    char_count = {}
    for i in word:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

count = char_frequency("mississippi")
print(count)

# Write a function celsius_list_to_fahrenheit(celsius_list) that takes a list of 
# Celsius temperatures and returns a NEW list with each one converted to Fahrenheit
# (reuse Day 1's formula: F = (C * 9/5) + 32, but applied across a list using a loop)

def celsius_list_to_fahrenheit(celsius_list):
    fahrenheit_list = []
    for i in (celsius_list):
        f = (i * 9/5) + 32
        fahrenheit_list.append(f)
    return fahrenheit_list
result1 = celsius_list_to_fahrenheit([6, 17, 32, 56])
print(result1)

# Find the student name with highest average

def top_student(students):
    best_name = None
    best_average = 0
    for student_id, info in students.items():
        marks = info["marks"]

        total = 0
        for mark in marks:
            total = total + mark

        average = total / len(marks)
        if average > best_average:
            best_average = average
            best_name = info["name"]
    print(f"Top student: {best_name} with average {best_average}")
    return best_name, best_average
best = top_student({
    "s1": {"name": "Pinank", "age": 33, "marks": [45, 66, 78]},
    "s2": {"name": "Rohan", "age": 36, "marks": [85, 44, 74]},
    "s3": {"name": "Raj", "age": 28, "marks": [66, 62, 70]}
})

# Find lowest priced Product
products = {
    "p1": {"name": "Laptop", "price": 55000},
    "p2": {"name": "Mouse", "price": 500},
    "p3": {"name": "Keyboard", "price": 1200}
}
lowest_price = None
best_name = None 
for products_id, info in products.items():
    name = info["name"]
    price = info["price"]  
    if lowest_price is None or price < lowest_price:
        lowest_price = price
        best_name = name
print(f"{best_name} is the lowest priced product at {lowest_price}")

#most frequent word
def most_frequent_word(sentence):
    new_split = sentence.split()
    word_count = {}
    for word in new_split:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    best_word = None
    best_count = None
    for word, count in word_count.items():
        if best_count is None or count > best_count:
            best_count = count
            best_word = word
    return best_word, best_count
result2 = most_frequent_word("the quick brown fox jumps over the lazy dog the fox runs")
print(result2)