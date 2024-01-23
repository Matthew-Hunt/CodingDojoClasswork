
def get_digits_from_string(string):
    digits_only = ''.join(filter(str.isdigit, string))
    return int(digits_only)

input_string = "0s1a3y5w7h9a2t4?6!8?0"
result = get_digits_from_string(input_string)
print(result)

