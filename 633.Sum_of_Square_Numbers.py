class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l=int(c**.5)
        if l**2==c:
            return True
        arr=list(range(1, l+1))
        i=0
        j=l-1
        while i<=j:
            if arr[i]**2+arr[j]**2==c:
                return True
            elif arr[i]**2+arr[j]**2<c:
                i+=1
            else:
                j-=1
            
        return False

        
