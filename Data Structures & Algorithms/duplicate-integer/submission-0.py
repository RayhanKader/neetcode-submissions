class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_dict = {}
        for i in range(len(nums)):
            if nums[i] in freq_dict:
                return True
            freq_dict[nums[i]] = 1
        return False
        
        