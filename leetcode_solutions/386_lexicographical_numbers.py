# https://leetcode.com/problems/lexicographical-numbers/description/
# 2025_06_08
# 386. Lexicographical Numbers
# PYthon

class Solution:
    def lexicalOrder(self, n: int) -> list[int]:

        res = []
        curr = 1
        
        for _ in range(n):
            res.append(curr)
        
            if curr * 10 <= n:
                curr *= 10
            else:
        
                if curr >= n:
                    curr //= 10
                curr += 1
        
                while curr % 10 == 0:
                    curr //= 10
        
        return res