def reverseParentheses(s):
    openParentheses = 0
    index = 0
    output = ""
    while openParentheses == 0:
        if s[index] == "(":
            print(index)
            openParentheses = 1
        index += 1
        print(index)

    while openParentheses == 1:
        if s[index] != "(" and s[index] != ")" and index <= len(s):
            print(s[index])
            output = output + s[index]
            print(output)
        elif s[index] == ")" and index <= len(s):
            if ")" not in s[index:]:
                openParentheses = 0
        index += 1

s = "a(bc)de"
reverseParentheses(s)
