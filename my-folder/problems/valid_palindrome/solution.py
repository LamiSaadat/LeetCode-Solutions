class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed = s[::-1]
        clean_s = ''.join(filter(str.isalnum, s.lower()))
        clean_reversed = ''.join(filter(str.isalnum, reversed.lower()))

        if clean_reversed == clean_s:
            return True
        else:
            return False