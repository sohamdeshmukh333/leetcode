# August 21, 2025
# Use a sliding window to track character frequencies, expanding the window for each character.
# When the window becomes invalid (requires more than k replacements), shrink it from the left.
class Solution(object):
   def characterReplacement(self, s, k):
       """
       :type s: str
       :type k: int
       :rtype: int
       """
       
       count = {}
       l = 0
       maxF = 0
       
       for r in range(len(s)):
           count[s[r]] = count.get(s[r], 0) + 1
           
           while (r - l + 1 - max(count.values())) > k:
               count[s[l]] -= 1
               if count[s[l]] == 0:
                   del count[s[l]]
               l += 1
           
           maxF = max(maxF, r - l + 1)
       
       return maxF
