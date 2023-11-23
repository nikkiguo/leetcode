class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1

        area = 0
        maxAmount = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxAmount = max(maxAmount, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxAmount


        