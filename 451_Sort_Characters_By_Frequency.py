class Solution:
    def frequencySort(self, s: str) -> str:
        m={}
        for char in s:
            if char not in m:
                m[char]=1
            else:
                m[char]+=1
        n=dict(sorted(m.items(), key=lambda x: x[1], reverse=True))
        a=''
        for key in n:
            a+=key*n[key]
        b=a
        return b
