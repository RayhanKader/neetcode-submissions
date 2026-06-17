class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_subarray = len(nums) + 1
        running_sum = 0
        for r in range(len(nums)):
            running_sum += nums[r]
            while running_sum >= target and l <= r:
                min_subarray = min(min_subarray, r-l+1)
                running_sum -= nums[l]
                l += 1
        return 0 if min_subarray == len(nums) + 1 else min_subarray
            


            