# https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
# 2025_06_29
# Encode and Decode Strings
# Python

class Solution:
    def enconde(self, strs: list[str]) -> str:
        
        '''
        The function returns an encoded list of strings.

        Args:
            strs: list[str]: List of string.
        
        Returns:
            return: str: Returns the strs list into a concatenated string with each substring's length and a # character attached at the beggining of each.
        '''

        result = ''

        for s in strs:
            result += str(len(s)) + '#' + s # Concatenating each substring's length and # sign before concatenating the next one.
        
        return result
        
    def decode(self, s: str) -> list[str]:

        '''
        The function returns a decoded string into a list of substrings.

        Args:
            s: str: String to be decoded.
        
        Returns:
            return: list[str]: Returns the initial string divided into substrings.
        '''

        result = []
        i = 0

        while i < len(s):   # i is the pointer that jumps from word to word
            j = i
            
            while s[j] != '#':  # j is the pointer that initially points to the end of the string's length
                j += 1
            
            length = int(s[i:j])    # length saves the substring's length so we can isolate each word depending on the previous # sign and it's own length
            i = j + 1
            j = i + length  # j and i now isolate each word using length as reference and j's position
            result.append(s[i:j])   # slicing the word in s and appending it to the result list
            i = j   # assigning i the beginning of the next substring's length number

        return result

    
sol = Solution()
strs = ["neet","code","love","you"]

print(sol.enconde(strs))
print(sol.decode(sol.enconde(strs)))