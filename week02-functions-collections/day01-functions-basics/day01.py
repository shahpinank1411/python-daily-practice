# 1. Write a function is_even(num) that RETURNS True if even, False if odd

def is_even(num):
    return num % 2 == 0
         
a =  is_even(5)
print(a)
b = is_even(4)
print(b)

# Write a function calculate_area(length, width) that returns the area of a rectangle

def calculate_area(length, width):
    area = length * width
    return area

a = 5
b =7
c = calculate_area(a,b)
print(f" Area of rectangle is {c}")

# Write a function is_prime(n) that returns True/False


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

a = is_prime(4)
b = is_prime(5)
c = is_prime(1)
d = is_prime(2)
print(a)
print(b)
print(c)
print(d)

#Write a function max_of_three(a, b, c) that returns the largest of three numbers

def max_of_three(a, b, c):
    if a == b == c:
        return a
    elif a == b:
        if a > c:
            return a
        else:
            return c
    elif a > b:
        if a > c:
           return a
        else:
            return c
    elif b > a:
        if b > c:
            return b
        else:
            return c

num = max_of_three(2,4,4)
print(num)

# Write a function celsius_to_fahrenheit(celsius) that returns the converted value
# formula: F = (C * 9/5) + 32

def cel_to_fahr(celcius):
    fahrenheit = (celcius*9/5) + 32
    return fahrenheit

result = cel_to_fahr(10)
print(result)