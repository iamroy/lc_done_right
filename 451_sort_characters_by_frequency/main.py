from collections import Counter
#451. Sort Characters By Frequency
def frequency_sort(s):
    char_counter = Counter(s)
    string_builder = []

    for letter, freq in char_counter.most_common():
        string_builder.append(letter * freq)

    return "".join(string_builder)

if __name__ == '__main__':
    s = "tree"
    s = "cccaaa"
    s = "Aabb"
    print(frequency_sort(s))