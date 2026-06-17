class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums_max = max(nums)
        nums_min = min(nums)
        nums_range = nums_max - nums_min + 1

        count = [0] * nums_range
        for num in nums:
            count[num - nums_min] += 1
        
        i = 0
        for c in range(len(count)):
            while count[c] != 0:
                nums[i] = c + nums_min
                i += 1
                count[c] -= 1
            