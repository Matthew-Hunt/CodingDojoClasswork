
def get_acronym(string):
    words = string.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

string1 = "there's no free lunch - gotta pay yer way."
result1 = get_acronym(string1)
print(result1)

string2 = "Live from New York, it's Saturday Night!"
result2 = get_acronym(string2)
print(result2)

