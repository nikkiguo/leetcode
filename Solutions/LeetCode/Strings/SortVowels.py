class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        change = []
        pos = []

        for i in range(len(s)):
            if s[i].lower() in vowels:
                change.append(ord(s[i]))
                pos.append(i)
        
        change = sorted(change)
        s = list(s)
        
        for i in range(len(pos)):
            s[pos[i]] = chr(change[i])
        
        return ''.join(s)
