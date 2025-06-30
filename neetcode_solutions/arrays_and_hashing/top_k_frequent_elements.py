# https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150
# 2025_06_29
# Top K Frequent Elements
# Python

class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:

        '''
        This function returns the k mos frequent numbers in nums.

        Args:
            nums: list[int]: List of numbers.
            k: int: Number of top elements to return.
        
        Returns:
            return: list[int]: Returns a list of size k with the k most frequent elements in nums.
        '''

        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]   # why '+ 1 '? I feel this creates one more space than needed.
                                                    # Each index represents the frequency of a num in nums. This is why.
                                                    # Each index has a sublist that will save all numbers in num that is repeated the index number of times

        # The hash map will save the frequency of each num, using the num as key.
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        # Each index of freq is a bucket. This loop will save all numbers to their correspoding frequencies.
        for num, count in hashmap.items():
            freq[count].append(num)
        
        # Result will be as big as k.
        result = []
        
        # Loop through frequency from last to beginning to save the k amount of nums.
        for i in range(len(freq) - 1, 0, -1): # range(start, stop, step)
            
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result


    
sol = Solution()
nums = [1,2,2,3,3,3]
k = 2

print(sol.top_k_frequent(nums, k))