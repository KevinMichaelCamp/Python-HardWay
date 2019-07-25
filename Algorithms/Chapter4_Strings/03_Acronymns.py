# Create a function that, given a string, returns the strings' acronym (first letters only, capitalized). Given " there's no free lunch - gotta pay your way. ", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN".

def acronymns(string):
    string = string.strip()
    acronym = string[0].upper()

    for i in range(1, len(string)):
        if string[i - 1] == " ":
            acronym += string[i].upper()
    return acronym


# Test Cases
print(acronymns(" there's no free lunch - gotta pay your way. "))
print(acronymns("Live from New York, it's Saturday Night!"))
