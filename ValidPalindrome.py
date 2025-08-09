class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newStr = ""
        s = s.strip()
        for c in s: 
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
