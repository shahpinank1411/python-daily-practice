# input 2 numbers - convert to int -add them
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)

#Simple Interest calculator
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time in years: "))
simple_interest = (principal * rate * time)/100
print(f"Total simple interest is {simple_interest}")

# swap 2 numbers/variables without using 3rd

a = 5
b = 6
a, b = b, a
print(a)
print(b)

# Check even or odd

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else: 
    print("The number is odd")