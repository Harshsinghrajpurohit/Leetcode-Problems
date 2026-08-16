class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_count=0
        count=0
        for i in accounts:
            count=sum(i)
            max_count=max(max_count,count)
        return max_count