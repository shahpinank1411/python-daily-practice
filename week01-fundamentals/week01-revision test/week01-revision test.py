# find if input number is positive negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number")
elif num == 0:
    print(f"{num} is zero")
else:
    print(f"{num} is a negative number ")

# count vowels in string

string = input("Enter a string: ")
Num_of_vowels = 0
for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i =="u":
        Num_of_vowels += 1
print(Num_of_vowels)

#prime numbers between 2 to 50
for n in range(2,51):
    is_prime = True
    for div in range(2,n):
        if n % div == 0:
            is_prime = False
            break
    if is_prime:
        print(n)

#count no of notes required

amount = int(input("Enter an amount: "))
r = amount % 500
q = amount // 500
print(f"no.of 500 notes required is {q}")
if r !=0:
    r1= r % 200
    q1= r // 200
    print(f"no.of 200 notes required is {q1}")
    if r1 !=0:
        r2= r1% 100
        q2= r1// 100
        print(f"no.of 100 notes required is {q2}")
        if r2 !=0:
            r3= r2 % 50
            q3= r2// 50
            print(f"no.of 50 notes required is {q3}")

# Reverse count from 100 which step of 7 and stop as it crosses 0

count = 100
while count >=  0:
    print(count)
    count -= 7

# determine a year is leap year or not and count no of leap years
years = int(input("Enter a year: "))
no_of_leap = 0
for i in range(2000, years+2000):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        no_of_leap += 1
        print(f"{i} is a leap year")
    else:
        print(f"{i} is not a leap year")
print(f"total no of leap years is {no_of_leap}")