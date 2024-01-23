def isCreditCardValid(digitArr):
    last_digit = digitArr[-1]
    digits = digitArr[:-1]

    for i in range(len(digits) - 1, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)

    total += last_digit

    return total % 10 == 0

digit_array = [5, 2, 2, 8, 2]
isValid = isCreditCardValid(digit_array)
print(isValid)
