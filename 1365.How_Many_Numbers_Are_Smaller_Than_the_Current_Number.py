class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=sorted(nums)
        l=len(nums)
        m={}
        n=[]
        for i in range(l):
            if i>=1 and s[i]==s[i-1]:
                continue
            m[s[i]]=i
        for i in range(l):
            n.append(m[nums[i]])
        return n
