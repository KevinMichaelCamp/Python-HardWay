# Assume that you have a text field that is exactly 75 characterics long. You want to fill it with spaces and asterisks ('*'). Print the given number of stars consecutively. Depending on which function is called, the stars should be left-justified, right-justified, or centered.

def drawLeftStars(num):
    text = ""
    text += "*" * num
    text += " " * (75 - num)
    return text


def drawRightStars(num):
    text = ""
    text += " " * (75 - num)
    text += "*" * num
    return text

def drawCenteredStars(num):
    text = ""
    text += " " * ((75 - num)//2)
    text += "*" * num
    return text

# Test Cases
print(drawLeftStars(35))
print(drawRightStars(35))
print(drawCenteredStars(35))
