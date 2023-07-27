# There are three types of edits that can be performed on strings: insert a character, remove a character, 
# or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

# Example:
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def same_length_func(s1, s2):
    # initialize a counter to keep track of edits between the two strings
    edit_counter = 0

    # going through each character in the length of s1 
    # if a character doesnt match in the two strings then increament the edit_counter by one
    # if edit_counter becomes greater than one then just return false because we can only have one edit.
    # if the strings make it through the whole for loop statment then just return True.
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            edit_counter += 1
            if edit_counter > 1:
                return False
    return True 

def different_length(word1, word2):
    # same as i = 0, and count = 0, less space.
    i = count = 0

    # while i (which starts at zero) is less than the length of word2 
    while i < len(word2):
        if word1[i + count] == word2[i]:
            i += 1
        else:
            count += 1
            if count > 1:
                return False
    return True

def one_away(s1, s2):
    # if the strings have a difference of more than 1 than its automatically more than one edit away.
    # so we take the difference of the absolute value of both strings and compare them in an if statement
    if abs(len(s1) - len(s2)) > 1:
        return False
    # else if length of strings are the same return same_length_func()
    elif len(s1) == len(s2):
        return same_length_func(s1, s2)
    # else if length of s1 is greater than s2 return different_length(s1, s2)
    elif len(s1) > len(s2):
        return different_length(s1, s2)
    # else if length of s1 is less than s2 return same different_length(s2, s1) function but reversed arguments.
    elif len(s1) < len(s2):
        return different_length(s2, s1)
    
s1 = "stringy"
s2 = "string"

print(one_away(s1, s2))