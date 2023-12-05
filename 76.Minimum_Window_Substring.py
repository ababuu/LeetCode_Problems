class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ct,wn={},{}
        for c in t:
            ct[c]=1+ct.get(c,0)
        i=0
        r,rl=[-1,-1],len(s)+1
        h,n=0,len(ct)
        for j in range(len(s)):
            wn[s[j]]=1+wn.get(s[j],0)
            if s[j] in ct and wn[s[j]]==ct[s[j]]:
                h+=1
            while h==n:
                if (j-i+1) < rl:
                    r=[i,j]
                    rl=j-i+1
                wn[s[i]]-=1
                if s[i] in ct and wn[s[i]]<ct[s[i]]:
                    h-=1
                i+=1
        return s[r[0]:r[1]+1]
        
