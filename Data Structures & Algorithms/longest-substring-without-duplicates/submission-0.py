class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        substring_map = {}
        max_length = 0
        if not s:
            return 0
        while i <= j and j < len(s):
            if s[j] in substring_map:
                substring_map.pop(s[i])
                i += 1
            else:
                substring_map[s[j]] = j
                curr_length = len(substring_map)
                max_length = max(curr_length, max_length)
                j += 1
        return max_length