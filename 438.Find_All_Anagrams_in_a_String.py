class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l_p=len(p)
        l_s=len(s)
        if l_s<l_p:
            return []
        arr=[]
        p_h=0
        s_h=0
        for i in range(l_p):
            p_h+=ord(p[i])*hash(p[i])
            s_h+=ord(s[i])*hash(s[i])
        for i in range(l_p,l_s):
            if p_h==s_h:
                arr.append(i-l_p)
            s_h=s_h-(ord(s[i-l_p])*hash(s[i-l_p]))+((ord(s[i])*hash(s[i])))
        if p_h==s_h:
            arr.append(l_s-l_p)
        return arr
