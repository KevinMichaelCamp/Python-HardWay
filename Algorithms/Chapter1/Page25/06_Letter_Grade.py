# Write a function that assigns and prints a letter grade, given an integer representing a score from 0 to 100. 90+ = A, 80-89 = B, 70-79 = C, 60-69 = D, < 60 = F. For example, given 88, print "Score: 88, Grade: B"

def letterGrade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Score:", score, "Grade:", grade)

# Test Cases
letterGrade(88)
letterGrade(59)
letterGrade(60)
