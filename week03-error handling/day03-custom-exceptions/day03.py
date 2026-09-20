# 1. Create a custom exception called NegativeNumberError.
#    Write a function square_root(n) that raises NegativeNumberError if n < 0,
#    otherwise returns n ** 0.5. Test both a valid and invalid input.

class NegativeNumberError (Exception):
    pass
def square_root(n):
    if n < 0:
        raise NegativeNumberError("Number is negative")
    return n ** 0.5
try:
    result = square_root(4)
except NegativeNumberError as e:
    print(f"Square root not possible : {e}")
else:
    print(f"Square root is : {result}")
try:
    result1 = square_root(-4)
except NegativeNumberError as e:
    print(f"Square root not possible : {e}")
else:
    print(f"Square root is : {result1}")


# 2. Write code that takes) user input and tries to convert it to an int, 
#    then divides 50 by it. Use a SINGLE except block that catches BOTH 
#    ValueError and ZeroDivisionError together (grouped with parentheses)

try:
    num = int(input("Enter a number: "))
    division = 50/num
except (ValueError, ZeroDivisionError) as e:
    print(f"Something is wrong: {e}")


# 3. Create a custom exception called InvalidPasswordError.
#    Write a function check_password(password) that raises this error if 
#    the password is shorter than 8 characters, otherwise returns "Password accepted"
#    Test with a short password and a valid one

class InvalidPasswordError(Exception):
    pass
def check_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Invalid Password")
    return password
try:
    check_password("123456")
except InvalidPasswordError as e:
    print (f"Unsucessful : {e}")
else:
    print("Password accepted")
try:
    check_password("12345678")
except InvalidPasswordError as e:
    print (f"Unsucessful : {e}")
else:
    print("Password accepted")


# 4. Write a function process_order(quantity, stock) that:
#    - raises a custom exception OutOfStockError if quantity > stock
#    - raises a custom exception InvalidQuantityError if quantity <= 0
#    - otherwise returns "Order processed"
#    Test all 3 cases, each in its own try/except

class OutOfStockError(Exception):
    pass
class InvalidQuantityError(Exception):
    pass
def process_order(quantity, stock):
    if quantity <= 0:
        raise InvalidQuantityError("Quantity must be Positive")
    elif quantity > stock:
        raise OutOfStockError("Not enough stock available")
    else:
        return "Order Processed"
try:
    print(process_order(-3, 10))
except InvalidQuantityError as e:
    print(f"Error: {e}")
else:
    print("Success")
try:
    print(process_order(15, 10))
except OutOfStockError as e:
    print(f"Error: {e}")
else:
    print("Success")

try:
    print(process_order(5, 10))
except (InvalidQuantityError, OutOfStockError) as e:
    print(f"Error: {e}")
else:
    print("Success")

# 5. Write a function that deliberately catches a ZeroDivisionError, 
#    prints "Logging error before crashing...", then RE-RAISES it 
#    (so the program still ultimately crashes with the original error)
#    Run it and observe that it still crashes, but AFTER printing your log message

def logging_error(a,b):
    div = a/b
    return div
try:
    result = logging_error(10,0)
except ZeroDivisionError:
    print("Logging: error before crashing")
    raise