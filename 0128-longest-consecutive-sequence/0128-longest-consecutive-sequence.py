class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set=set()
        for i in range(0,len(nums)):
            my_set.add(nums[i])
        longest=0
        for num in my_set:
            if num-1 not in my_set:
                x=num
                count=1
                while num+1 in my_set:
                    count+=1
                    num+=1
                longest=max(longest,count)
        return longest        