# Given an integer, return an integer that is the reverse ordering of numbers.
# example:
# reverseInt(15) = 51
# reverseInt(500) = 5
# reverseInt(-90) = -9

def reversed_int(num):
    # convert into a string
    string = str(num)

    # adding string to a list
    string = list(string)
    # reverse the string
    string.reverse()
    # join reversed list back into a string
    string = ''.join(string)

    # convert string into int.
    number = int(string)

    return number

# numb = -90
# print(reversed_int(numb))


# solution 2.
def reversed_int(num):
    # convert into a string
    string = str(num)

    # if the start of the string begins with '-'
    if string[0] == '-':
        # take the reverse of the string and replace ending zeros with nothing 
        rev_neg = string[::-1].replace('0', '')
        # then return a formatted string with the '-' at the beginning and the reversed string after.
        return f"{string[0]}{rev_neg[:-1]}"
    # else, just return the reversed string.
    else:
        return string[::-1]
    

numb = -2304
print(reversed_int(numb))

