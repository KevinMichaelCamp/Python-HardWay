# Given a sequence of parenthesis, braces, and brackets, determine wether string is valid. Example: "W(a{t}s[o(n{ c}o)m] ) h[e{r}e]!" => True. "D(i{a}l [ t] o)n{e" => False. "A(1)s[o(n]0{t) 0}k]" => False

def bracesValid(str):
    open = ['(', '{', '[']
    close = [')', '}', ']']
    stack = []

    for char in str:
        if char in open:
            stack.append(char)
        elif char in close:
            pos = close.index(char)
            if len(stack) > 0 and open[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


# Test Cases
print(bracesValid("W(a{t}s[o(n{ c}o)m] ) h[e{r}e]!"))
print(bracesValid("D(i{a}l [ t] o)n{e"))
print(bracesValid("A(1)s[o(n]0{t) 0}k]"))
