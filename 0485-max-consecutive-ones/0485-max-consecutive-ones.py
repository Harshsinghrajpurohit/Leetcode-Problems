class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_count=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
            else:
                max_count=max(max_count,count) # here we find the maximum of count and max_count
                count=0
        return max(max_count,count) # ahain a final maximum of count and max_count
