class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def freq_dict(string):
            string_dict = {}
            for char in string:
                if char not in string_dict:
                    string_dict[char] = 0
                string_dict[char] += 1
            return string_dict
        
        s_anagram = freq_dict(s)
        t_anagram = freq_dict(t)

        return s_anagram == t_anagram
        
                