class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        res = []

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        mapsort = list(sorted(hashmap.items(), key=operator.itemgetter(1), reverse = True))
        for i in range(k):
            res.append(mapsort[i][0])

        return res
        
        