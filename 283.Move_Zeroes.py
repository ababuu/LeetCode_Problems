class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)>1:
            i=0
            j=1
            while j<len(nums):
                if nums[i]==0 and nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                elif nums[i]==0 and nums[j]==0:
                    j+=1
                    continue
                j+=1
                i+=1
                    

            

        
