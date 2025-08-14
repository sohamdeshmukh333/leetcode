# August 14, 2025
# Use a set for O(1) lookups and only start counting from sequence beginnings (numbers without predecessors).
# For each sequence start, count consecutive numbers until no next number exists in the set.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        numSet = set(nums)
        maxLen = 0
        
        for n in numSet:
            # Only start counting if this is the beginning of a sequence
            if (n - 1) not in numSet:
                count = 1
                nextInt = n + 1
                
                while nextInt in numSet:
                    count += 1
                    nextInt += 1
                
                maxLen = max(maxLen, count)
        
        return maxLen
