"""
1.2 Check Permutation: 
Given two strings, write a method to decide if one is a permutation of the other.
"""

def checkPermutation(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: bool
    """
    str1 = list(str1)
    str2 = list(str2)
    
    str1.sort()
    str2.sort()

    return str1 == str2
