# https://neetcode.io/problems/is-anagram?list=neetcode150
# 2025_06_27
# Valid Anagram
# Python

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        
        '''
        Function will return true or false if t is an anagram of s.

        Args:
            s: str: String.
            t: str: Could be an anagram of s.
        
        Returns:
            return: bool: True if t is an anagram of s.
        '''
        
        if len(s) != len(t): # First check if both strings have the same length
            return False
        
        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1 # Increment the frequency of each character used in the string
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1 # hash.get(key, default) will default to the default value if key isn't found

        return hash_s == hash_t

        '''
        Sorting (brute force solution)
        
        return sorted(s) == sorted(t)
        '''


sol = Solution()
print(sol.is_anagram('anagram', 'aaangrm'))
