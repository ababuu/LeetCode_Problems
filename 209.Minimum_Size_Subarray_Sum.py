class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        l=len(nums)
        output=l+1
        s=0
        for j in range(l):
            s+=nums[j]
            while s>=target:
                output=min(output,j-i+1)
                s-=nums[i]
                i+=1
        return output%(l+1)
            
