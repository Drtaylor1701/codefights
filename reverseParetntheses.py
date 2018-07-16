def reverseParentheses(s):
    parenthesesLocations = []
    index = 0
    for letter in s:
        if letter == "(" or letter == ")":
            parenthesesLocations.append(index)
            print(parenthesesLocations)
        index += 1

    openClose = len(parenthesesLocations) / 2
    openClose = int(openClose)
    print(openClose)

    open = parenthesesLocations[openClose]
    close = parenthesesLocations[openClose + 1]
    print(open, close)

    middle = s[open:close]
    print(middle)
s = "a(bc)de"
reverseParentheses(s)
