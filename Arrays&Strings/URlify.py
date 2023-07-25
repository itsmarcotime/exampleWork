# Write a method to replace all spaces in a string with "%20", assume there is suficient space at the end.
# ignore ending white spaces.

# input: "Mr John Smith    ", 13
# output Mr%20John%20Smith

# function will be passed a "string" and n the size of the string 
# this has a runtime of O(a*b) because we are dealing with 2 varying variables.
# the number of words that go into the list, and the number of spaces that need to be replaced. 
# because these two factors vary we have a runtime of O(a*b)
def URLify(string, n):
    # string[:n] cuts off all characters after the nth term.
    # .split() splits words by using spaces and stores each word in a list
    cut_off_space = string[:n].split()
    # this will concatenate the words we stored in cut_off_space with "%20" between each word.
    result = "%20".join(cut_off_space)
    return result

string = "hi how are you    "
n = 14
print(URLify(string, n))
