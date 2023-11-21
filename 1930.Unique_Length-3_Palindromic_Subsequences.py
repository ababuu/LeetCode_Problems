class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(s)
        f=[len(s)]*26
        l=[0]*26
        count=0
        for i,c in enumerate(s):
            index=ord(c)-ord('a')
            f[index]=min(f[index],i)
            l[index]=max(l[index],i)
        for i in range(26):
            if f[i]<l[i]:
                q=set(s[f[i]+1:l[i]])
                count+=len(q)
        return count
