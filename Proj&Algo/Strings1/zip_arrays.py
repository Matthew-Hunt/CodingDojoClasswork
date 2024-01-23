
def create_dictionary(arr1, arr2):
    dictionary = dict(zip(arr1, arr2))
    return dictionary

arr1 = ["abc", 3, "yo"]
arr2 = [42, "wassup", True]
result = create_dictionary(arr1, arr2)
print(result)
