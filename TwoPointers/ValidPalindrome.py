# Date: August 14, 2025
# This solution checks if a string is a palindrome by using two pointers from opposite ends.
# It ignores non-alphanumeric characters and performs case-insensitive comparison.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def alphaNum(self,c):
        if(
            ord("0") <= ord(c) <= ord("9") or
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") 
        ):
            return True
        return False
