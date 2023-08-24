# Given a String, find the first non-repeating charater in it and return its index.
# If it doesn't exist, return -1

# example:
# s= 'leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

# 1. create a unique map and insert characters 
# 2. if the same character is seen again, set that mapping to flase
# 3. iterate over the string and check in map if that charcter is set to true, if yes return Index
# 4. if no unique characters return -1

def unique_character(str):
    unique_map = {}

    # loop through the string
    for i in range(0, len(str)):
        # if character in string is not in map, add it to map and set it to true.
        if str[i] not in unique_map:
            unique_map[str[i]] = True
        # else, the character has already appeared so character value in map is set to false.
        else:
            unique_map[str[i]] = False

    # loop back over string
    for i in range(0, len(str)):
        if unique_map[str[i]]:
            return i
    return -1

string = "leetcode"
print(unique_character(string))