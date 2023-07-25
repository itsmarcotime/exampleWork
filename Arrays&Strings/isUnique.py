#ARRAYS AND STRINGS

# Implemment an algorith to determine whether a string has all unique characters.
# What if you cannot use additional data structures?

# solution1 brute force
def is_unique(string):
    # deleting whitespace
    string = string.replace(" ", "")
    # conver to lower case
    string = string.lower()
    # check length of string
    if len(string) > 256:
        return False
    else:
        return len(string) == len(set(string))
    
# print(is_unique('abc'))



# solution2 hash tables
def is_unique(string):
    # deleting whitespace
    string = string.replace(" ", "")
    # conver to lower case
    string = string.lower()
    # check length of string
    if len(string) > 256:
        return False
    else:
        char_set = {}
        for i in string:
            if i in char_set:
                return False
            else:
                char_set[i] = True
        return True
    
# print(is_unique("abc"))




# solution3 brute force pt. 2

def is_unique(string):
    # deleting whitespace
    string = string.replace(" ", "")
    # conver to lower case
    string = string.lower()
    # check length of string
    if len(string) > 256:
        return False
    else:
        for i in range(len(string)):
            for j in range(i + 1, len(string)):
                if string[i] == string[j]:
                    return False
        return True
    
# print(is_unique("abc"))





#ARRAYS AND STRINGS

# Implemment an algorith to determine whether a string has all unique characters.
# What if you cannot use additional data structures?

# brute force runtime of O(n^2)
def is_unique(s):
    list = []

    for i in s:
        if i not in list:
            list.append(i)
    
    if len(s) != len(list):
        return False
    else:
        return True
    
s = 'string'
print(is_unique(s))

# int div(int a, int b) {
#     int count = 0;
#     int sum = b;
#     while (sum <= a) {
#         sum += b;
#         count++;
#     }
#     return count;
# }


