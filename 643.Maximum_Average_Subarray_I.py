class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l=len(nums)
        s=sum(nums[:k])
        max_s=s
        for i in range(k,l):
            s=s+nums[i]-nums[i-k]
            if s>max_s:
                max_s=s
        return (max_s+.00)/k
