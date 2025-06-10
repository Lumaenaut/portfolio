# https://leetcode.com/problems/roman-to-integer/description/
# 2025_06_09
# 13. Roman to Integer
# PYthon

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i, j in zip(s, s[1:]):
            
            if roman_map[i] < roman_map[j]:
                result -= roman_map[i]
            else:
                result += roman_map[i]

        result += roman_map[s[-1]]
        
        return result
    
solu = Solution()
solu.romanToInt('IV')