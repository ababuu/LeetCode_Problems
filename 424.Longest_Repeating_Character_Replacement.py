class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s=list(s)
        l=len(s)
        max_char=0
        memo={}
        j=0
        i=0
        while i <l:
            if s[i] not in memo:
                memo[s[i]]=1
            else:
                memo[s[i]]+=1
            max_char=max(max_char,memo[s[i]])
            if i-j-max_char+1>k:
                memo[s[j]]-=1
                j+=1
            i+=1
        return min(max_char+k,l)
