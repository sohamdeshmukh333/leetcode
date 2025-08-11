class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hashS, hashT = {},{}

        for c in s:
            if not c in hashS:
                hashS[c] = 1
            else:
                hashS[c] += 1
        for c in t:
            if not c in hashT:
                hashT[c] = 1
            else:
                hashT[c] += 1

        return hashS == hashT


    

        

    
