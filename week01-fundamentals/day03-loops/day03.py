#grading system

marks = int(input("Please Enter your marks: "))

if marks >= 90:
    print("Your grade is A")
elif marks >= 75:
    print("Your grade is B")
elif marks >=50:
    print("Your grade is C")
else:
    print("Your grade is F")

# Login system

user_name = input("Please enter your user name: ")
password = input("Please enter your password: ")

if user_name == "admin" and password == "1234":
    print("Access Granted")
else:
    print("Access Denied")

#Leap Year

year = int(input("Please enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Greatest of 3

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is the greatest")
    elif num1 == num3:
        print(f"{num1} and {num3} are equal")
    else:
        print(f"{num3} is the greatest")
elif num2 > num1:
    if num2 > num3:
        print(f"{num2} is the greatest")
    elif num2 == num3:
        print(f"{num2} and {num3} are equal")
    else:
        print(f"{num3} is the greatest")
elif num3 > num1:
    if num3 > num2:
        print(f"{num3} is the greatest")
    else:
        print(f"{num2} is the greatest")
elif num1 == num2 == num3:
    print(f"{num1}, {num2} and {num3} are equal")
else:
    print(f"{num1} and {num2} are equal")


signal = input("Enter Signal: ")

if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Get Ready")
elif signal == "Green":
    print("Go")
else:
    print("Invalid signal")