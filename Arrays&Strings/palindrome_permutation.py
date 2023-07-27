# Given a string write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwords and backwards. A permuation 
# is a rearrangement of letter. The palindrome does not need to be limited to just dictionary words.

# input: Race Car
# output: True (Permuations: "taco cat", "atcp cta", etc.)

# 2 2 2 1 2 2 2
# r a c e c a r

palindrome = "rACE cAR"
not_palindrome =" This is not a palindrome permutation"

# the runtime of this function is O(n)
# the space complexcity is also O(n)
def palindrome_permutation(input_string):
    input_string = input_string.replace(" ", "")
    input_string = input_string.lower()

    # using hash tables here so initialize the dictionary to be used.
    d = dict()

    # for each character in input string..
    for i in input_string:
        # if character is in dictionary the increment its value by 1
        if i in d:
            d[i] += 1
        # otherwise give the character an initial value of 1
        else:
            d[i] = 1
    
    # we can only have up to 1 odd value for a palindrome so we need to keep track of the odd instances.
    odd_count = 0

    # for the key value pairs in each item in the dictionary.. 
    for k, v in d.items():
        # if the value we encounter in the loop is odd AND the odd_count = 0, then increment odd counter by 1
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        # else if the value is odd AND odd_count is not equal to 0
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(palindrome_permutation(palindrome))
print(palindrome_permutation(not_palindrome))


