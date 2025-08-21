# August 19th, 2025
# Uses sliding window technique with two pointers (l, r) and a set to track unique characters
# Expands window by moving right pointer, shrinks from left when duplicates found, tracks max length
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

