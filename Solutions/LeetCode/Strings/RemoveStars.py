class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []

        for char in s:
            if char == '*':
                res.pop()
            else:
                res.append(char)
        
        return ''.join(res)