
def is_anagram(s, t):
    squares = dict()
    for element in s:
        if element in squares.keys():
            squares[element] += 1
        else:
            squares[element] = 1

    for element in t:
        if element in squares.keys():
            squares[element] -= 1

            if squares[element] == 0:
                squares.pop(element)
        else:
            return False

    res = not bool(squares)

    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "rat"
    t = "cat"
    print(is_anagram(s, t))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
