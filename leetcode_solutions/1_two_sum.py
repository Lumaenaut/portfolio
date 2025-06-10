# https://leetcode.com/problems/two-sum/description/
# 2025_06_06
# 1. Two Sum
# PYthon

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        hashmap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
        
            if complement in hashmap:
                return [hashmap[complement], i]
        
            hashmap[nums[i]] = i
        
        return []