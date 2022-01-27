
def is_valid_parentheses(s):

    stack = []
    parent_map = {")":"(", "]": "[", "}":"{"}
    stack_top = []

    for v in s:

        if v in parent_map.keys():
            if stack:
                stack_top = stack[-1]
                if stack_top != parent_map[v]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        else:
            stack.append(v)

    return not stack


if __name__ == '__main__':
    s = "{[]}"
    print(is_valid_parentheses(s))