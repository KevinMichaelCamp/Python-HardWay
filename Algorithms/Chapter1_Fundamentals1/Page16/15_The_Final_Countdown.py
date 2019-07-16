# This is based on "Flexible Countdown". The parameter names are not
# as helpful, but the problem is essentially identical. Given 4
# parameters (param1, param2, param3, param4), print the multiples
# of param1, starting at param2 and extending to param3. One exeption:
# if a multiple is equal to param4, then skip (don't print) that one.
# Do this using a WHILE loop.  Given (3,5,17,9) print 6,12,15 (which 
# are all the multiples of 3 between 5 and 17, except for the value 9.

def finalCountdown(param1, param2, param3, param4):
    i = param2

    while i <= param3:
        if i == param4:
            i += 1
            continue
        elif i % param1 == 0:
            print(i)
        i += 1


# Test Cases
finalCountdown(3,5,17,9)
finalCountdown(7,0,100,77)
