# Basic
for i in range(151):
    print(i)

# Multiples of Five
for m in range(5, 1001, 5):
    print(m)

# Counting, the Dojo Way
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

# Whoa. That Sucker's Huge
total = 0

for num in range(1, 500001, 2):
    total += num

print("The sum of odd integers from 0 to 500,000 is:", total)

# Countdown by Fours
num = 2018

while num > 0:
    print(num)
    num -= 4

# Flexible Counter

lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)