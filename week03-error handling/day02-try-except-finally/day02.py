# 1. Write code that asks the user for two numbers and divides them.
#    Handle BOTH ValueError (non-numeric input) and ZeroDivisionError, 
#    with distinct messages for each

try:
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    result = num1/num2
    print(result)
except ValueError:
    print("The number is not a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


# 2. Write a function safe_get_item(my_list, index) that tries to return 
#    my_list[index], but catches IndexError and returns "Index out of range" instead
#    Test with a valid index AND an invalid one (e.g. index 10 on a 3-item list)

def safe_get_item(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return "Index out of Range"

my_list = [10, 20, 30]
print(safe_get_item(my_list, 1))
print(safe_get_item(my_list, 10))

# 3. Write a function validate_age(age) that raises a ValueError with message 
#    "Age cannot be negative" if age < 0, and "Age seems unrealistic" if age > 120
#    Otherwise, return the age. Test all 3 cases (negative, too large, valid) 
#    wrapping each call in try/except

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Age seems unrealistic")
    else:
        return age
try:
    print(validate_age(-1))
except ValueError as e:
    print(f"Error : {e}")

try:
    print(validate_age(135))
except ValueError as e:
    print(f"Error : {e}")

try:
    print(validate_age(25))
except ValueError as e:
    print(f"Error : {e}")


# 4. Write code that tries to open a file that doesn't exist ("fake_file.txt"), 
#    catches the specific error (hint: FileNotFoundError), and prints a friendly message
#    instead of crashing

try:
    file = open("fake_file.txt")
except FileNotFoundError:
    print("Sorry, that file doesn't exist!")

# 5. Write a function safe_divide(a, b) using try/except/else/finally — 
#    it should: try the division, catch ZeroDivisionError with a message, 
#    use else to print the result if successful, and use finally to print 
#    "Division attempt complete" every single time

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by Zero")
    else:
        print(result)
    finally:
        print("Division attempt complete")
safe_divide(2,3)
safe_divide(2,0)   
    