class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Hashmap
        prevMap = {} #{key:value} -> {diff:index}
        
        for i, n in enumerate(nums):
            diff = target - n
            if n in prevMap:
                return[prevMap[n],i]
            prevMap[diff] = i #add value in Hashmap
