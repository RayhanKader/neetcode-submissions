class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_seen = {}
        for string in strs:
            str_count = tuple(sorted(string))
            if str_count in strs_seen:
                strs_seen[str_count].append(string)
            else:
                strs_seen[str_count] = [string]
        
        return list(strs_seen.values())