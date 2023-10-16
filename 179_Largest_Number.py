class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        compare=lambda x,y: -1 if x+y>y+x else 1
        nums.sort(key=cmp_to_key(compare))
        return str(int(''.join(nums)))
