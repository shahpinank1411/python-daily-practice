# print 1 to 20 but stop when divisble by 13
for i in range(1,21):
    if i % 13 ==0:
        break
    print(i)

# Print 1 to 20 skip all numbers divisble by 3
for i in range(1,21):
    if i % 3 ==0:
        continue
    print(i)

# reverse pyramid
n = 5
for i in range(1, n+1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# number triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#find and print 1-100 where 1st number is divisble by 7 & 5

for i in range(1,101):
    if i % 5 == 0 and i % 7 ==0:
        print(i)
        break