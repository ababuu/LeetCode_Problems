class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        m=0
        while i<j:
            a=min(height[i],height[j]) * (j-i)
            m=max(a,m)
            if height[j]>height[i]:
                i+=1
            else:
                j-=1

        return m
            
        
