# Create clockHandAngles(seconds) that, given a number of seconds since 12:00:00, prints angles (in degrees) of the hour, minute and second hands. As review, 360 degrees form a full rotation. For an input of 3600 secs (equivalent to 1 hr) print "Hour hand: 30 degs. Minute Hand: 0 degs. Second Hand: 0degs."

def clockHandAngles(seconds):
    time = seconds

    # Weeks
    weeks =  time / 1680
    time = time % 604800
    # Hours
    hours = time / 120
    time = time % 3600
    # Minutes
    minutes = time / 10
    seconds = time % 60
    # seconds
    seconds = seconds * 6

    print("Weeks: ", weeks, chr(176), sep='')
    print("Hours: ", hours, "\xb0", sep='')
    print("Minutes: ", minutes, "\xb0", sep='')
    print("Seconds: ", seconds, "°", sep='')


# Test Cases
print("Test Case 1", '\n', '*'*50)
clockHandAngles(3600) # 1hr
print("Test Case 1", '\n', '*'*50)
clockHandAngles(23400) # 6hr, 30min
print("Test Case 1", '\n', '*'*50)
clockHandAngles(26440) # 7hrs, 20min, 40sec
