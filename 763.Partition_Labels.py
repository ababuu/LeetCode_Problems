class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        i=0
        l=len(s)-1
        j=l
        h_map={}
        r=[]
        while i<=j:
            if s[i] in h_map:
                h_map[s[i]]=max(i,h_map[s[i]])
            else:
                h_map[s[i]]=i
            if s[j] in h_map:
                h_map[s[j]]=max(j,h_map[s[j]])
            else:
                h_map[s[j]]=j
            i+=1
            j-=1
        m=0
        p=-1
        for k in range(l+1):
            m=max(m,h_map[s[k]])
            if m==k:
                r.append(m-p)
                p=m
        return r
                

            



        
