class Solution(object):
    def mergeAlternately(self, word1, word2):
        m= len(word1)
        n= len(word2)
        i, j= 0,0
        merge=[]
        while i<m or j<n:
            if i< m:
                merge.append(word1[i])
                i+=1
            if j<n:
                merge.append(word2[j])
                j+=1
        return ''.join(merge)
            

        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        