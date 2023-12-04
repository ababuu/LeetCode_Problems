class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s,t,i,d=0,0,0,{0:1}
        while i<len(nums):
            s+=nums[i]
            if s-k in d:
                t+=d[s-k]
            if s in d:
                d[s]+=1
            else:
                d[s]=1
            i+=1
        return t 
        
