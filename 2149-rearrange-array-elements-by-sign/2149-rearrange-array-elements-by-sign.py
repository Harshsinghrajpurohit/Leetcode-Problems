class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        pos_idx=0
        neg_idx=1
        for i in range(0,n):
            if nums[i]>=0:
                res[pos_idx]=nums[i]
                pos_idx+=2
            else:
                res[neg_idx]=nums[i]
                neg_idx+=2
        return res