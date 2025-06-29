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

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for num, count in hashmap.items():
            freq[count].append(num)
        
        result = []
        
        for i in range(len(freq) - 1, 0, -1):
            
            for num in freq[i]:
                result.append(num)
                print(result)
                print(len(result))
                if len(result) == k:
                    return result


    
sol = Solution()
nums = [1,2,2,3,3,3]
k = 2

print(sol.top_k_frequent(nums, k))