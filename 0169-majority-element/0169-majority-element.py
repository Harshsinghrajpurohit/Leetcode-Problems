class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ans = -1       # Current candidate
        count = 0      # Candidate's current vote balance

        for num in nums:

            # If count becomes 0,
            # choose the current number as the new candidate
            if count == 0:
                ans = num

            # Same as candidate → candidate gets +1 vote
            if ans == num:
                count += 1

            # Different from candidate → cancel one vote
            else:
                count -= 1

        return ans