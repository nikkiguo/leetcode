class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        idx = 0
        n = 1
        res = []

        while idx < len(target):
            if n == target[idx]:
                res.append("Push")
                idx += 1
            else:
                # for "missing" elements of target
                res.append("Push")
                res.append("Pop")
            n += 1

        return res
