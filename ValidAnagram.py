class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for c in range(len(s)):
            countS[s[c]] = 1 + countS.get(s[c],0)
            countT[t[c]] = 1 + countT.get(t[c],0)

        for i in countS:
            if countS[i] != countT.get(i,0):
                return False
        return True
        
