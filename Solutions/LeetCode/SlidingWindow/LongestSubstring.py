class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)

        if sLen == 0:
            return 0
        
        if sLen == 1:
            return 1

        l = r = 0
        maxLen = 1
        occurMap = {}
 
        while r < sLen:
            if s[r] in occurMap:
                l = max(occurMap[s[r]], l)
            maxLen = max(maxLen, r - l + 1)
            occurMap[s[r]] = r + 1
            r += 1
        return maxLen

