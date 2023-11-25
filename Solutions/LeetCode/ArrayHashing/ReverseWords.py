class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        processed = s.split()[::-1]
        return ' '.join(processed)
        