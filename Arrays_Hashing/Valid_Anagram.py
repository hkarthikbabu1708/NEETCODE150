# Given two strings s and t, return true if the two strings are anagrams of each other,
# otherwise return false.
# An anagram is a string that contains the exact same characters as another string,
# but the order of the characters can be different.

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    if sorted(s) != sorted(t):
        return False

    return True

# s = "racecar"
# t = "carrace"
s = "jar"
t = "jam"
print(isAnagram(s,t))