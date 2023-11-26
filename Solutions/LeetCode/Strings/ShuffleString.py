class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        strLen = len(s)
        res = [''] * strLen

        for i in range(strLen):
            res[indices[i]] = s[i]

        return ''.join(res)