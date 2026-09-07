# 1. Create a dictionary representing yourself (name, age, city, favorite_language).
#    Print each value using .get(), including one key that doesn't exist 
#    (with a sensible default), to prove .get() doesn't crash.

myself = {"name" : "Pinank",
          "age": 33,
          "city": "Mumbai",
          "language" : "English"}
print(myself.get("name"))
print(myself.get("age"))
print(myself.get("city"))
print(myself.get("language"))
print(myself.get("sports" , "N/A"))

# Write a function count_vowels_dict(string) that returns a dictionary counting
# how many times EACH vowel (a,e,i,o,u) appears in the string.
# e.g. count_vowels_dict("banana") → {'a': 3}  (only include vowels that actually appear)

def count_vowels_dict(vowels):
    vowels_count = {}
    for vowel in vowels:
        if vowel in "aeiou":
            if vowel in vowels_count:
               vowels_count[vowel] += 1
            else:
               vowels_count[vowel] = 1
    return vowels_count

result = count_vowels_dict("the quick brown fox jumps over the lazy dog")
print(result)
print(count_vowels_dict("banana"))

# Take this sentence: "the quick brown fox jumps over the lazy dog the fox runs"
# Split it into words (hint: string.split()) and build a dictionary counting 
# how many times each word appears.

sentence = "the quick brown fox jumps over the lazy dog the fox runs"
new_split = sentence.split()
word_count = {}
for word in new_split:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# Create a nested dictionary representing 3 students, each with name, age, and marks (a list of 3 numbers).
# Loop through it and print each student's name along with their AVERAGE marks 
# (calculate manually, don't use a library).

students = {
    "s1": {"name": "Pinank", "age": 33, "marks": [45, 66, 78]},
    "s2": {"name": "Rohan", "age": 36, "marks": [85, 44, 74]},
    "s3": {"name": "Raj", "age": 28, "marks": [66, 62, 70]}
}

for student_id, info in students.items():
    name = info["name"]
    marks = info["marks"]

    total = 0
    for mark in marks:
        total = total + mark

    average = total / len(marks)
    print(f"{name}'s average marks: {average}")

    # Given two dictionaries:
# prices = {"apple": 50, "banana": 20, "mango": 80}
# quantities = {"apple": 3, "banana": 5, "mango": 2}
# Write code to calculate and print the TOTAL cost (price × quantity, summed across all items)

prices = {"apple": 50, "banana": 20, "mango": 80}
quantities = {"apple": 3, "banana": 5, "mango": 2}

total_cost = 0
for fruit in prices:
    price = prices[fruit]
    quantity = quantities[fruit]
    total_cost = total_cost + (price * quantity)
print(total_cost)