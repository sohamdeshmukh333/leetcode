# August 26, 2025
# This solution uses the sliding window technique with two pointers to find the minimum window substring.
# It expands the window by moving the right pointer, then shrinks from the left when a valid window is found.

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, have = {}, {}
        for c in t:
            need[c] = need.get(c,0)+1
        
        l,r=0,0
        min_len = len(s) + 1
        min_str = ""

        while r < len(s):
            have[s[r]] = have.get(s[r],0) + 1

            valid = True
            for char in need:
                if have.get(char,0) < need[char]:
                    valid = False
                    break
            if valid:
                while valid: 
                    current_len = r - l + 1
                    if current_len < min_len:
                        min_len = current_len
                        min_str = s[l:r+1]
                    
                    have[s[l]] -= 1
                    l += 1

                    valid = True
                    for char in need:
                        if have.get(char,0) < need[char]:
                            valid = False
                            break
            r += 1 

                
        return min_str
                



            









            
        



