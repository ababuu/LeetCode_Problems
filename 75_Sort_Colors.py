class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,i,r=0,0,len(nums)-1
        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                i+=1
                l+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[r],nums[i]=nums[i],nums[r]
                r-=1
