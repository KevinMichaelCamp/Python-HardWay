# Based on earlier "Countdown by Fours", given lowNum, highNum, mult,
# print mulitples of mult from highNum down to lowNum, using a FOR.
# For (2,9,3) print 9 6 3 (on successive lines)

def flexibleCountdown(lowNum, highNum, mult):
    for i in range(highNum, lowNum, -1):
        if i % mult == 0:
            print(i)
            
# Test Cases
flexibleCountdown(2,9,3)
flexibleCountdown(0,100,7)
