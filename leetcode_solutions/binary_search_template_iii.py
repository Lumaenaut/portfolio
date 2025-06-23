# https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
# 2025_06_23
# Binary Search
# Template III
# Python


# Finding the peak element

class Solution:
    def find_peak_element(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left


nums = [7,6,6,6,5,4]
sol = Solution()
print(sol.find_peak_element(nums))


'''
**********************************************************************************************************

2025_06_22

# Finding the k numbers closest to x

class Solution:
    def find_closest_elements(self, arr: list[int], k: int, x: int) -> list[int]: # change return to -> list[int]
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


arr = [1,2,3,4,5,8,9,10,11,12,13,14]
k = 7 # quantity
x = 8 # target

sol = Solution()
print(sol.find_closest_elements(arr, k, x))

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
