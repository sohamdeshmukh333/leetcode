class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        wordList = []
        for word in strs:
            wordChar = {}
            for c in word:
                if not c in wordChar:
                    wordChar[c] = 1
                else: 
                    wordChar[c] += 1
            wordList.append(wordChar)

        output = []
        visited = set()
        #print(wordList)
        for i in range (len(strs)):
            if i in visited:
                continue
            group = [strs[i]]
            visited.add(i)
            
            for j in range (i+1, len(strs)): 
                if j not in visited and wordList[i] == wordList[j]:
                    group.append(strs[j])
                    visited.add(j)
                    print(j)
            output.append(group)

        return output
            
            

                

        
        
