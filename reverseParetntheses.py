def reverseParentheses(s):
    index = 0
    while index < len(s):
        if s[index] == "(" or s[index] == ")":
            print(s[index], index)
            index += 1
        else:
            print("there are no parentheses")

s = "a(bc)de"
reverseParentheses(s)
