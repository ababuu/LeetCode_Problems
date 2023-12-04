class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l=len(arr)
        i=0
        cm=0
        output=1
        for j in range(l-1):
            new_cm=(arr[j]>arr[j+1])-(arr[j]<arr[j+1])
            if new_cm!=0 and new_cm!=cm:
                cm=new_cm
            else:
                output=max(output,j-i+1)
                i=j+(arr[j]==arr[j+1])
        return max(l-i,output)
