# 1. Take a messy string: "   Hello, World!   " 
#    Clean it (strip whitespace), then print it in uppercase AND lowercase

string = "   Hello, World!   " 
new_string = string.strip()
print(new_string)
print(new_string.upper())
print(new_string.lower())

# 2. Write a function is_palindrome(word) that returns True/False
#    A palindrome reads the same forwards and backwards (e.g. "madam", "racecar")
#    Hint: you already know how to reverse a string manually from Week 1 — 
#    or try using slicing: word[::-1]

def is_palindrome(word):
    return word == word[::-1]
result = is_palindrome("racecar")
print(result)
result2 = is_palindrome("hello")
print(result2)

# 3. Take this CSV-style string: "Pinank,25,Mumbai,Python"
#    Split it into a list, then print each value on its own line with a label
#    (Name: Pinank, Age: 25, City: Mumbai, Language: Python)

csv_string = "Pinank,25,Mumbai,Python"
word = csv_string.split(",")
name, age, city, language = word
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City : {city}")
print(f"Language : {language}")

# 4. Write a function word_count(sentence) that returns how many words are in a sentence
#    (don't overthink it — think about what split() naturally gives you)

def word_count(sentence):
    new_sentence = sentence.split()
    count1 = len(new_sentence)
    return count1
new_word = word_count("the quick brown fox")
print(new_word)

# 5. Take a sentence and replace every occurrence of a specific word with another word,
#    then also count how many replacements were made
#    e.g. "I love cats and cats love me" → replace "cats" with "dogs"
#    print the new sentence AND how many replacements happened (hint: use count() first)

sentence = "I love cats and cats love me"
replacement_count = sentence.count("cats")   # count BEFORE replacing
new_sentence = sentence.replace("cats", "dogs")

print(new_sentence)
print(f"Replaced 'cats' {replacement_count} times")