# https://neetcode.io/problems/anagram-groups?list=neetcode150
# 2025_06_28
# Group Anagrams
# Python

class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        
        '''
        Function will return a list of anagram sublists.

        Args:
            strs: list[str]: List of strings.
        
        Returns:
            return: list[list[str]]: A list of anagram sublists.
        '''
        
        hashmap = {}

        for s in strs:
            hash_key = [0] * 26

            for c in s:
                hash_key[ord(c) - ord('a')] += 1

            hash_key = tuple(hash_key)
            
            if hash_key not in hashmap:
                hashmap[hash_key] = [] # You can use immutables as keys in a dictionary
            
            hashmap[hash_key].append(s)

        return list(hashmap.values())

        '''
        This is a naive way of solving it.
        I'm creating a string by sorting the word and using it as a key for future anagrams.
        I'm also sorting several times, which doesn't make it look clean.
        
        hashmap = {}
        result_list = []
        
        for i in strs:

            if str(sorted(i)) not in hashmap:
                hashmap[str(sorted(i))] = [i]
            else:
                hashmap[str(sorted(i))].append(i)

        for key in hashmap:
            result_list.append(hashmap[key])
        
        return result_list
        '''
        
    
strs_1 = ["act","pots","tops","cat","stop","hat"]
strs_2 = ['x']
strs_3 = ['']

sol = Solution()
print(sol.group_anagrams(strs_1))