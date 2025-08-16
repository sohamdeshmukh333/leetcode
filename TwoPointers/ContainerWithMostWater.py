# August 16, 2025
# I used the two-pointer technique with left and right pointers starting at opposite ends of the array.
# The key insight was to always move the pointer pointing to the shorter line, since keeping it would never yield a larger area.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxA = 0
        l,r = 0, len(height) - 1

        while l < r:
            diff = r - l
            if height[l] < height[r]:
                maxA = max(maxA, (diff * height[l]))
                l += 1
            else: 
                maxA = max(maxA, (diff * height[r]))
                r -= 1
        return maxA 
