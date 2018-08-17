# Python - The Hard Way - Exercise 10 - Escape Sequences

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fatter_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fatter_cat

# All Python Escape Characters

# print "\\"                      # Backslash (\)
# print "\'"                      # Single-quote (')
# print "\""                      # Double-quote (")
# print "\abell"                  # ASCII bell (BEL)
# print "back\bspace"             # ASCII backspace (BS)
# print "\fFormfeed"              # ASCII formfeed (FF)
# print "\nLineFeed"              # ASCII linefeed (LF)
# print "\N{BLACK SPADE SUIT}"    # Character named name in the Unicode database
# print "\rCarraige Return"       # ASCII carraige return (CR)
# print "\tHorizontal tab"        # ASCII horizontal tab (TAB)
# print "\uxxxx"                  # Character with 16-bit hex value xxxx
# print "\Uxxxxxxxx"              # Character with 32-bit hex value Uxxxxxxxx
# print "\vVertical tab"          # ASCII Vertical tab (VT)
# print "\ooo"                    # Character with octal value oo
# print "\xhh"                    # Character with hex value hh

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i
