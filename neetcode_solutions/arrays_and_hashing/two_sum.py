# https://neetcode.io/problems/two-integer-sum?list=neetcode150
# 2025_06_28
# Two Sum
# Python

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        
        '''
        Function that returns a pair of indexes that point to the values in nums that sum to target.
        The problem guarantees target will always be the result of only one sum between only two numbers in nums.

        Args:
            nums: list[int]: List of numbers.
            target: int: Result of a sum between two numbers in nums.
        
        Returns:
            return: list[int]: Returns the pair of indexes that point to the values that sum up to target.
        '''

        hashmap = {}
    
        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[nums[i]] = i

    
nums = [3,4,5,6]
target = 7

sol = Solution()

print(sol.two_sum(nums, target))
