class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1=len(word1)
        l2=len(word2)
        i=0
        j=0
        m=[]
        while i<l1 and j<l2:
            if word1[i]>word2[j]:
                m.append(word1[i])
                i+=1
            elif word1[i]<word2[j]:
                m.append(word2[j])
                j+=1
            else: 
                if word1[i+1:]>=word2[j+1:]:
                    m.append(word1[i])
                    i+=1
                else:
                    m.append(word2[j])
                    j+=1
        if i<l1:
            m.extend(word1[i:])
        elif j<l2:
            m.extend(word2[j:])
        return ''.join(m)
