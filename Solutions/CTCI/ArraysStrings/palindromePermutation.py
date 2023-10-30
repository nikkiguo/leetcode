"""
1.4 Palindrome Permutation: 
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is 
the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""

def palindromePermutation(s):
    """
    :type s: str
    :rtype: bool
    """
    s = list(s)
    charDict = {}
    letterCount = 0 

    for letter in s:
        if charDict.get(letter.lower()):
            charDict[letter.lower()] += 1
        else:
            charDict[letter.lower()] = 1
    
    for k in charDict:
        if charDict[k] == 1 and k != ' ':
            letterCount += 1
    
    return letterCount <= 1
