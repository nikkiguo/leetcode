class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)
        n = list(n)

        return n == n[::-1]
        