# https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
# 2025_06_14
# Binary Search
# Template I
# Python


# Find the target in an rotated list

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)

            if nums[mid] == target:
                print('first')
                return mid
            
            # Check if left half is ordered
            if nums[left] <= nums[mid]:
                print('second')

                # Check if number is in ordered range
                if nums[left] <= target < nums[mid]:
                    print('second, first')
                    right = mid - 1
                else:
                    print('second, second')
                    left = mid + 1
            else:
                print('third')

                if nums[mid] < target <= nums[right]:
                    print('third, first')
                    left = mid + 1
                else:
                    print('third, second')
                    right = mid - 1

        return -1

nums_one = [5, 1, 3]

sol = Solution()
print(sol.search(nums_one, 3))


'''
**********************************************************************************************************

2025_06_13

Guessing the picked number within a range of integers

def guess(n: int) -> int:
    
    if n == num: return 0
    elif n > num: return -1
    return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        mid = 0
        
        while left <= right:
            mid = (left + right) // 2
                    
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1
    
num = 986 # picked number
ran = 10000 # range of numbers
s = Solution()

print(s.guessNumber(ran))

**********************************************************************************************************

2025_06_12

Searching for the closest whole number of the root of x without using square or root operands

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0 or x == 1:
            return x
        
        left, right = 0, x
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                answer = mid
                break
            elif mid * mid < x:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer

**********************************************************************************************************
        
2025_06_12

Searching for target in a nums list using binary search

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        guess = 0
        left, right = 0, len(nums) - 1
        
        while left <= right:
            guess = (right + left) // 2
            
            if nums[guess] == target:
                return guess
            else:
                
                if nums[guess] < target:
                    left = guess + 1
                else:
                    right = guess - 1
        
        return -1

**********************************************************************************************************
'''