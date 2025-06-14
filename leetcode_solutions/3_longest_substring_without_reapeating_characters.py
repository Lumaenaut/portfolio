# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# 2025_06_11
# 3. Longest Substring Withour Repeating Characters
# Python

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        substring = set()
        length = 0

        while i < len(s):
            
            if s[i] not in substring:
                substring.add(s[i])
                length = max(len(substring), length)
                i += 1
            else:
                substring.remove(s[j])
                j += 1
        
        return length