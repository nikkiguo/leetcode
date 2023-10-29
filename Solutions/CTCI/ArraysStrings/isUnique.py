"""
1.1 Is Unique: 
Implement an algorithm to determine if a string has all unique characters. 
"""

def isUnique(s):
    """
    :type s: str
    :rtype: bool
    """
    letterDict = {}
    for l in s:
        if letterDict.get(l):
            return False
        else:
            letterDict[l] = 1
    return True

"""
1.1 Is Unique: 
What if you cannot use additional data structures? 
"""
def isUnique(s):
    """
    :type s: str
    :rtype: bool
    """
    s = list(s)
    s.sort()

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True
