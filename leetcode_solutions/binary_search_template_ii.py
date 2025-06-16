# https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
# 2025_06_15
# Binary Search
# Template II
# Python




'''
2025_06_15

def is_bad_version(version: int) -> bool:
    
    if bad_version <= version:
        return True
    
    return False

class Solution:
    def first_bad_version(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2

            if is_bad_version(mid):
                print(left, mid, right, True)
                right = mid
            else:
                print(left, mid, right, False)
                left = mid + 1
            
        return left

bad_version = 1
versions = 1

sol = Solution()
print(sol.first_bad_version(versions))
'''