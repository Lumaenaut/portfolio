# https://leetcode.com/problems/palindrome-number/
# 2025_06_08
# 9. Palindrome Number
# Python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        s = str(x)
        r = s[::-1]


        if s == r : 
            return True
        else: 
            return False
        
        