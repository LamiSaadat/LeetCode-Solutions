from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create an empty set
        charSet = set()
        #index of the left most element
        left_pointer = 0
        result = 0

        #loop through the string by checking the right most pointer
        for right_pointer in range(len(s)):
            #while the right most pointer is in the set
            while s[right_pointer] in charSet:
                #remove the left most pointer from the set
                charSet.remove(s[left_pointer])
                #update the pointer index
                left_pointer += 1
            #once the duplicates have been removed, add the current element to the set
            charSet.add(s[right_pointer])
            #the result will be the longest of the current result or the length of the substring left in the window
            result = max(result, right_pointer - left_pointer +1)
        return result