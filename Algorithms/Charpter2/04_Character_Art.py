# From star art - do the same but allow for character to be passed in as argument

def drawLeftStars(num, char):
    text = ""
    text += char * num
    text += " " * (75 - num)
    return text


def drawRightStars(num, char):
    text = ""
    text += " " * (75 - num)
    text += char * num
    return text

def drawCenteredStars(num, char):
    text = ""
    text += " " * ((75 - num)//2)
    text += char * num
    text += " " * ((75 - num)//2)
    return text

# Test Cases
print(drawLeftStars(35, "%"))
print(drawRightStars(35, "@"))
print(drawCenteredStars(35, "!"))
