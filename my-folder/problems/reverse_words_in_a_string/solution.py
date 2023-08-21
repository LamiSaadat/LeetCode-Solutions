class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split()).split(" ")
        l = 0
        r = len(s) - 1

        while (l < r):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
        return " ".join(s)