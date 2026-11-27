class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        curr_sum = nums[0]
        best_sum = nums[0]

        for i in nums[1:]:
            curr_sum = max(i, curr_sum + i)
            best_sum = max(best_sum, curr_sum)

        return best_sum
        