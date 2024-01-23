
def invertHash(assocArr):
    inverted = {value: key for key, value in assocArr.items()}
    return inverted

assocArr = {"name": "Zaphod", "charm": "high", "morals": "dicey"}
result = invertHash(assocArr)
print(result)

