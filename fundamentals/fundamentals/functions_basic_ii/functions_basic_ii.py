
#1

def countdown(n):
    result = []
    for i in range(n, -1, -1):
        result.append(i)
    return result

print(countdown(5))


#2

def print_and_return(lst):
    print(lst[0])
    return lst[1]

result = print_and_return([1, 2])
print(result)

#3

def first_plus_length(lst):
    return lst[0] + len(lst)

result = first_plus_length([1, 2, 3, 4, 5])
print(result)

#4

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    second_val = lst[1]
    greater_vals = [val for val in lst if val > second_val]
    count = len(greater_vals)
    print(count)
    return greater_vals

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5

def length_and_value(size, value):
    if size < 1:
        return False
    return [value] * size

print(length_and_value(4, 7))
print(length_and_value(6, 2))
print(length_and_value(0, 5))