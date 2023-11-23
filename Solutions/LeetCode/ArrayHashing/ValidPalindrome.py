class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = lower(s).replace(" ", "")
        filteredS = ""

        for i in range(len(s)):
            if s[i].isalnum():
                filteredS += s[i]
            
        l = 0
        r = len(filteredS) - 1

        while l < r:
            if not filteredS[l].isalnum():
                l += 1
            if not filteredS[r].isalnum():
                r -= 1
            if filteredS[l] == filteredS[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        