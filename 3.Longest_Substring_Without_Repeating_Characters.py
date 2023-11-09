class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        if l == 0:
            return 0
        s=list(s)
        k=0
        j=0
        memo={}
        for i in range(l):
            if s[i] in memo and memo[s[i]]>=j:
                j=memo[s[i]]+1
            memo[s[i]]=i
            k=max(k,i-j+1)
        return k
