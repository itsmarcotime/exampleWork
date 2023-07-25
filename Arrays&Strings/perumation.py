# Given two strings write a method to decide if one is a permutation of the other.
# "driving"
# "drivign" <-- Permuation
# "ddriving" <-- not a perumation
# "riving" <-- not a perumation
# "criving" <-- not a perumation

# need clarifcation for spacing
# "the cow jumps over the moon"
# "the moon jumps over the cow" <-- permutation
# "the moon          jumps over the cow" <-- if spacing is considered a character then this is not a permutation.

# this is O(a * b) runtime because we are not sure of the length of each string.
s1 = "driving"
s2 = "drivign"

def find_permutation(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if i in s2:
            s2 = s2.replace(i, "")

    return len(s2) == 0

print(find_permutation(s1, s2))


