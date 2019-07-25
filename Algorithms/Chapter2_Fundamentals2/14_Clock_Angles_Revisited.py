# Allow fractional values for input seconds, but print only integer values for angles of clock hands.

def clockHandAngles(seconds):
    time = seconds

    # Weeks
    weeks =  time // 1680
    time = time % 604800
    # Hours
    hours = time // 120
    time = time % 3600
    # Minutes
    minutes = time // 10
    seconds = time % 60
    # seconds
    seconds = seconds * 6

    print("Weeks: ", weeks, chr(176), sep='')
    print("Hours: ", hours, "\xb0", sep='')
    print("Minutes: ", minutes, "\xb0", sep='')
    print("Seconds: ", seconds, "°", sep='')


# Test Cases
print("Test Case 1", '\n', '*'*50)
clockHandAngles(3600.5) # 1hr
print("Test Case 1", '\n', '*'*50)
clockHandAngles(23400.2) # 6hr, 30min
print("Test Case 1", '\n', '*'*50)
clockHandAngles(26440) # 7hrs, 20min, 40sec
