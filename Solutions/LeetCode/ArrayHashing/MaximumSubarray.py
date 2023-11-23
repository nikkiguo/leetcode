class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumSoFar = 0
        maxSum = nums[0]
        
        for num in nums:
            if sumSoFar < 0:
                sumSoFar = 0
            sumSoFar += num
            maxSum = max(maxSum, sumSoFar)
        return maxSum

        