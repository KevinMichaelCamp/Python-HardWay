# Create a function that, given an input string str, returns a boolean whether parenthesis in str are valid. Valid sets of parenthesis always open before they close, and all open parens have a close, for example - "Y(3(p)p(3)r)s" return True. For "M(0(p)3" return False - not every parameter is closed.

def parensValid(str):
    open_count, close_count = 0, 0

    for char in str:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
        if close_count > open_count:
            return False
    if open_count != close_count:
        return False

    return True

    print(stack)


# Test Cases
print(parensValid("Y(3(p)p(3)r)s"))
print(parensValid("M(0(p)3"))
