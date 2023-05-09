# Create a function that, given a string, returns all of that string’s contents, but without blanks. 
# If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".
def remove_blanks(string):
    return ''.join(string.split())

string =  " Pl ayTha tF u nkyM usi c "
result = remove_blanks(string)
print(result)

# Create a JavaScript function that given a string, returns the integer made from the string’s digits. 
# Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.
def get_digits(string):
    digits = ''.join(filter(str.isdigit, string))
    return int(digits)

string=( "0s1a3y5w7h9a2t4?6!8?0")
result = get_digits(string)
print(result)

# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). 
def acronym(string):
    words = string.split()
    acronym = ''.join(word[0].upper()for word in words)
    return acronym
string = "World Health Organization"
result = acronym(string)
print(result)

#  Given two arrays, create an associative array (map) containing keys of the first, and values of the second.
# For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.
def zip_arrays_into_dctionary(arr1, arr2):
    return dict(zip(arr1, arr2))
arr1 = ["abc", 3, "yo"]
arr2 =  [42, "wassup", True]
result = zip_arrays_into_dctionary(arr1,arr2)
print(result)

#  Build invertHash(assocArr) to convert hash keys to values, and values to keys. 
def invert_hash(hash):
    inverted_hash = {value: key for key, value in hash.items()}
    return inverted_hash

my_dict =  {"name": "Zaphod", "charm": "high", "morals": "dicey"}
result = invert_hash(my_dict)
print(result)