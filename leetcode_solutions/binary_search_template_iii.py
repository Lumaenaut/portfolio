# https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
# 2025_06_20
# Binary Search
# Template III
# Python

# Finding the range of the same value within a list

class Solution:
    def search_range(self, nums: list[int], target: int) -> list[int]:
        first = -1
        last = -1        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
            if nums[mid] == target:
                first = mid 
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

            if nums[mid] == target:
                last = mid

        return [first, last] if first != -1 and last != -1 else [-1, -1]

nums = [0,0,0,0,2,2,4,5,5,5,5,5,8,9,9,9,10]
target = 10

sol = Solution()
print(sol.search_range(nums, target))


'''
**********************************************************************************************************

2025_06_20

Finding the range of the same value within a list

class Solution:
    def search_range(self, nums: list[int], target: int) -> list[int]:
        first = -1
        last = -1        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
            if nums[mid] == target:
                first = mid 
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

            if nums[mid] == target:
                last = mid

        return [first, last] if first != -1 and last != -1 else [-1, -1]

**********************************************************************************************************
'''
