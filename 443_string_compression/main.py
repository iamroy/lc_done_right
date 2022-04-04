#443. String Compression
#Input: chars = ["a","a","b","b","c","c","c"]
#Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
def compress_string(chars):
    ptr1 = 0
    ptr2 = 0
    ptr3 = -1

    while ptr1<len(chars):
        c = chars[ptr1]

        if ptr1 == ptr2:
            ptr3 += 1
            chars[ptr3] = c
            ptr2 += 1
            while ptr2<len(chars):
                if c == chars[ptr2]:
                    ptr2 += 1
                else:
                    break

        char_len = ptr2-ptr1
        char_len_str = str(char_len)

        if char_len>1:
            for i in range(len(char_len_str)):
                ptr3 += 1
                chars[ptr3] = char_len_str[i]
        ptr1 = ptr2

    return ptr3+1

if __name__ == '__main__':
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(compress_string(chars))
    print(chars)