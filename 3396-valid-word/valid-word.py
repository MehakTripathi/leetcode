class Solution(object):
    def isValid(self, word):
        n= len(word)
        count=0
        c, v= 0,0
        vow= "aeiouAEIOU"
        if n < 3 or not word.isalnum():
            return False

        for i in range(n):
            if word[i].isalpha():
                if word[i] in vow:
                    v+=1
                    count+=1
                else:
                    c+=1
                    count+=1
            elif word[i].isdigit():
                count+=1
                 
        return v>=1 and c>=1
                
               





        """
        :type word: str
        :rtype: bool
        """
        