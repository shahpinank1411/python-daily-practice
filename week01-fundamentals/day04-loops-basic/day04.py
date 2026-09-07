# Print numbers from 1 to 10

for i in range(1,11):
    print(i)

for i in range(2,52,2):
    print(i)

n = int(input("Enter a num: "))
total = 0
for i in range(1,n+1):
    total = total + i
print(f" Sum of first {n} natural numbers is {total}")

n = int(input("Enter a number: "))
for i in range(1,11):
    mul = n * i
    print(mul)

n = "Pinank"
reverse_n = ""

for i in range(len(n) -1, -1, -1):
    reverse_n = reverse_n + n[i]

print(reverse_n)

secret = 7
guess = int(input("Guess the number: "))

while guess != secret:
    guess = int(input("Wrong! Guess the number again: "))

print("Correct")