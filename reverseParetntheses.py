def reverseParentheses(s):
    index = 0
    while index < len(s):
        if s[index] == "(" or s[index] == ")":
            print(s[index])

s = "a(bc)de"
reverseParentheses(s)