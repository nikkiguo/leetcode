class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left = []
        middle = []
        right = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] == pivot:
                middle.append(nums[i])
            else:
                right.append(nums[i])
    
        return left + middle + right
        


        