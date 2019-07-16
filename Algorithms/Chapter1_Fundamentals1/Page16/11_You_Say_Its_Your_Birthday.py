#If 2 given numbers represent your birth month and day in either order,
#print "How did you know?", otherwise print "Just another day..."

def birthday(num1, num2):
    if (num1 == 11 and num2 == 20) or (num2 == 11 and num1 == 20):
        print('How did you know?')
    else:
        print('Just another day...')

num1 = int(input("Enter 1st number > "))
num2 = int(input("Enter 2nd number > "))
birthday(num1, num2)
