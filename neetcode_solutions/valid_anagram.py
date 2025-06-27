# https://neetcode.io/problems/is-anagram?list=neetcode150
# 2025_06_27
# Valid Anagram
# Python

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        
        '''
        Function will return true or false if there are any duplicates in nums.

        Args:
            nums: list[int]: List of integers that may or may not contain duplicates.
        
        Returns:
            return: bool: True if there are duplicates in nums. False otherwise.
        '''
        
        if len(s) != len(t):
            return False
        
        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1

        return hash_s == hash_t

        '''
        Sorting (brute force solution)
        
        return sorted(s) == sorted(t)
        '''


sol = Solution()
print(sol.is_anagram('anagram', 'aaangrm'))

