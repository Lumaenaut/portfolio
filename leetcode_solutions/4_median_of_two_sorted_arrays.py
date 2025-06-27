# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# 2025_06_25
# 4. Median of Two Sorted Arrays
# Python

# First apprach. Brute force.
# Concatenate both lists, sort them, and find the middle value if length of list is odd. If length is even, average both values

class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        sum_list = nums1 + nums2
        sum_list.sort()

        if len(sum_list) % 2 == 0:
            print(sum_list[len(sum_list) // 2])
            print(sum_list[len(sum_list) // 2 - 1])
            return (sum_list[len(sum_list) // 2] + sum_list[len(sum_list) // 2 - 1]) / 2
        
        return sum_list[len(sum_list) // 2]
    
li1 = [5,6,7,8,9]
li2 = [1,10,15,16,18]

sol = Solution()
print(sol.find_median_sorted_arrays(li1, li2))


'''
**********************************************************************************************************

# 2025_06_24

# First apprach. Brute force.
# Concatenate both lists, sort them, and find the middle value if length of list is odd. If length is even, average both values

class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        sum_list = nums1 + nums2
        sum_list.sort()

        if len(sum_list) % 2 == 0:
            print(sum_list[len(sum_list) // 2])
            print(sum_list[len(sum_list) // 2 - 1])
            return (sum_list[len(sum_list) // 2] + sum_list[len(sum_list) // 2 - 1]) / 2
        
        return sum_list[len(sum_list) // 2]
        
**********************************************************************************************************
'''