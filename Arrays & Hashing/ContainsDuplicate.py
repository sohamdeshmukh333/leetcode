class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Hashmap
        intMap = {} #{value:count}

    
        for n in nums:
            if not n in intMap: 
                intMap[n] = 1
            else: #duplicate is found
                return True 
        return False
