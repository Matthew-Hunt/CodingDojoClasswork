def combine_arrays(arr1, arr2):
    combined = []
    for a, b in zip(arr1, arr2):
        combined.extend([a, b])

    combined.extend(arr1[len(arr2):])
    combined.extend(arr2[len(arr1):])

    return combined


array1 = [4, 15, 100]
array2 = [10, 20, 30, 40]
result = combine_arrays(array1, array2)
print(result)
