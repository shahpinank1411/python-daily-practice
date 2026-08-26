# Write a lambda that checks if a number is even, assign it to a variable is_even_lambda

is_even_lambda = lambda n: n % 2 ==0
print(is_even_lambda(3))
print(is_even_lambda(4))

# 1. Write a function power(base, exponent=2) that returns base raised to exponent
#    Test it calling with just base (should square it), and with both args

def power(base, exponent = 2):
    result = base ** exponent
    return result

print(power(3))
print(power(2,5))

# Write a function multiply_all(*numbers) that returns the product of all numbers passed in
# (like add_all above, but multiplication — careful about the starting value!)

def multiply_all(*numbers):
    result = 1
    for n in numbers:
        result = result * n
    return result

print(multiply_all(1,4,5,7))

# Write a function print_student(**info) that prints each key-value pair
# Test with print_student(name="Pinank", age=25, course="Python")

def print_student(**info):
    for key, value in info.items():
        print(f"{key} : {value}")

print_student(name = "Pinank", age = 25, course = "Python")

# Write a function order_summary(customer_name, *items, **details)
# that prints the customer name, all items ordered, and any extra details (like discount, address)
# Test: order_summary("Pinank", "Laptop", "Mouse", discount="10%", city="Mumbai")

def order_summary(customer_name, *items, **details):
    print(f"Customer: {customer_name}")
    
    print("Items ordered:")
    for item in items:
        print(item)
    
    print("Additional details:")
    for key, value in details.items():
        print(key,":", value)

order_summary("Pinank", "Mouse", "Laptop", discount = "10%", city = "Mumbai")