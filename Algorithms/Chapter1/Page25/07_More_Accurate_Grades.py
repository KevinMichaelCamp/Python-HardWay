# Add '+' and '-' to the bottom and top 2% of letter grades

def letterGrade(score):
    if score > 97:
        grade = "A+"
    elif score > 92:
        grade = "A"
    elif score > 89:
        grade = "A-"

    elif score > 87:
        grade = "B+"
    elif score > 82:
        grade = "B"
    elif score > 79:
        grade = "B-"

    elif score > 77:
        grade = "C+"
    elif score > 72:
        grade = "C"
    elif score > 69:
        grade = "C-"

    elif score > 67:
        grade = "D+"
    elif score > 62:
        grade = "D"
    elif score > 59:
        grade = "D-"

    else:
        grade = "F"

    print("Score:", score, "Grade:", grade)

# Test Cases
letterGrade(88)
letterGrade(60)
letterGrade(59)
letterGrade(85)
