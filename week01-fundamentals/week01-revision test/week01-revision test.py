years = int(input("Enter a year: "))
no_of_leap = 0
for i in range(2000, years+2000):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        no_of_leap += 1
        print(f"{i} is a leap year")
    else:
        print(f"{i} is not a leap year")
print(f"total no of leap years is {no_of_leap}")