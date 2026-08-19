class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        current=0

        while current<=high:
            if nums[current]==0:
                nums[low],nums[current]=nums[current],nums[low]
                low+=1
                current+=1
            elif nums[current] == 2:
                nums[high],nums[current]=nums[current],nums[high]
                high-=1
            else:
                current+=1