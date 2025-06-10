# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/
# 2025_06_07
# 386. Lexicographically Minimum String After Removing Stars
# PYthon

class Solution:
    def clearStars(self, s: str) -> str:

        count = [[] for _ in range(26)]
        array = list(s)
        
        for i, a in enumerate(array):
        
            if a != '*':
                count[ord(a) - ord('a')].append(i)
            else:
        
                for j in range(26):
        
                    if count[j]:
                        array[count[j].pop()] = '*'
                        break
        
        return ''.join(c for c in array if c != '*')