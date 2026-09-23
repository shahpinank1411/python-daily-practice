import random
def calculator():
    print("\n---calculator---")
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operation = input("Choose Operation (+, -, *, /): ")
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            print("Invalid Operation")
            return
        print(f"The Result is {result}")
    except ValueError:
        print("Please enter valid number")
    except ZeroDivisionError:
        print("Cannot divide by Zero")


def guessing_game():
    print("\n---Number Guessing Game---")
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 to 100: "))
        except ValueError:
            print("Please Enter a Valid Number")
            continue
        attempts += 1
        if guess < secret:
            print("Too Low")
        elif guess > secret:
            print("Too High")
        else:
            print(f"Correct. You got it in {attempts} attempts")
            break

def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Calculator")
        print("2. Number Guessing Game")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            guessing_game()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

main_menu()