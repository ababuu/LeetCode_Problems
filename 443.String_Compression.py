class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=1
        j=1
        c=1
        while j<len(chars):
            if chars[j-1]==chars[j]:
                j+=1
                c+=1
            else:
                if c>1:
                    for k in str(c):
                        chars[i]=k
                        i+=1
                chars[i]=chars[j]
                i+=1
                j+=1
                c=1
        if c>1:
            for k in str(c):
                chars[i]=k
                i+=1
        chars=chars[:i]
        return len(chars)
