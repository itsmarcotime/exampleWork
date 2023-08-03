# Implement a method to perform basic string compression using the counts of repeated characters.
# for example, the string aabbccdd would become a2b2c2d2. If the compressed string would not become 
# smaller than the the original string, your method should return the original string. You can assume 
# the string has only uppercase and lowercase letters (a-z).

def string_compression(string):
    # all values will be put into a list so we can iterate over them.
    compressed_values = [string[0]]
    # the count starts at 1 because we assume that there is at least one value in the string being passed.
    count = 1

    # for each charater in the range of 1 to the length of the string...
    # we start at 1 becasue the count starts at 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed_values.extend([count, string[i]])
            count = 1
    compressed_values.append(count)

    result = "".join(map(str, compressed_values))

    return result
    

string = 'aaabbbcccccccddddeeeeeee'

compressed_string = string_compression(string)

if len(compressed_string) < len(string):
    print(compressed_string)
else:
    print(string)