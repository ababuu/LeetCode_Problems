class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1=len(s1)
        l2=len(s2)
        if l2<l1:
            return False
        c1=[0]*26
        c2=[0]*26
        a=ord('a')
        i=0
        while i< l1:
            c1[ord(s1[i])-a]+=1
            c2[ord(s2[i])-a]+=1
            i+=1
        i=0
        j=l1
        while j<l2:
            if c1==c2:
                return True
            c2[ord(s2[i])-a]-=1
            c2[ord(s2[j])-a]+=1
            i+=1
            j+=1
        if c1==c2:
            return True
        return False
        
