# Threes and Fives
# Write a function ThreesFives() that add each value from
# 100 to 4000 (inclusive) if that value is evenly divisible
# by 3 or 5 but not both. Return the final sum.

def ThreesFives():
    total = 0
    for num in range(100, 4001):
        if num % 3 == 0 and num % 5 != 0:
            total += num
        elif num % 3 != 0 and num % 5 == 0:
            total += num
    return total

print(ThreesFives())