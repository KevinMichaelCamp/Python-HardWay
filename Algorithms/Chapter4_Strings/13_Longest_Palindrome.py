# Return the longest palindrome found in a string.

def longestPalindrome(str):
    max_length = 1
    start, low, high = 0, 0, 0


    for i in range(1, len(str)):
        # For even number length palindromes
        low = i - 1
        high = i

        while low >= 0 and high < len(str) and str[low] == str[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

        # For odd number length palindromes
        low = i - 1
        high = i + 1

        while low >= 0 and high < len(str) and str[low] == str[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

    print("Longest palindrome is", str[start:start + max_length])
    print(max_length)
    return str[start:start + max_length]


# Test Cases
print(longestPalindrome("Yikes! My favorite racecar erupted!"))
