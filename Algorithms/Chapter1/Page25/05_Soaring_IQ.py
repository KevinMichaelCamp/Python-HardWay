# A student enters the Dojo with an IQ of 101. Let's say during the 14 week bootcamp, his IQ rose by .01 on the first day, then went up an additional .02 on the second day, and so on all the way to .98 on the 98th day. What is the final IQ?

IQ = 101

for i in range(99):
    IQ += (.01 * i)
    print(IQ)

print(IQ)
