class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        l = 0
        r = len(nums) - 1

        maxSum = 0

        while l < r:
            maxSum = max(nums[l] + nums[r], maxSum)
            l += 1
            r -= 1

        return maxSum
        