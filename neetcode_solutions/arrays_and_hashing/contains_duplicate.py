# https://neetcode.io/problems/duplicate-integer?list=neetcode150
# 2025_06_27
# Contains Duplicate
# Python

class Solution:
    def has_duplicate(self, nums: list[int]) -> bool:
        
        '''
        Function will return true or false if there are any duplicates in nums.

        Args:
            nums: list[int]: List of integers that may or may not contain duplicates.
        
        Returns:
            return: bool: True if there are duplicates in nums. False otherwise.
        '''
        
        hashset = set(nums) # If nums has duplicates they won't be stored in hashmap. Next line will take advantage of this.

        return len(hashset) < len(nums) # Since hashmap won't have duplicates nums' length will be greater.

        '''
        Brute force solution.

        hashmap = set()

        for i in nums:
            
            if i in hashmap:
                return True
            hashmap.add(i)

        return False
        '''


nums = [1,2,3,3]
sol = Solution()

print(sol.has_duplicate(nums))