import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s=s.replace(' ','')
        for punctuation in string.punctuation:
            s = s.replace(punctuation, "")
        s=s.lower()
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
        
