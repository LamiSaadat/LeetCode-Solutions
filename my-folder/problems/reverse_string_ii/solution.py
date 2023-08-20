class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for i in range(0, len(s), 2*k):
            subStr = s[i:i+2*k]
            subStr2 = subStr[:k][::-1]
            revSub = subStr.replace(subStr[:k], subStr2)
            s = s.replace(subStr, revSub)
        return s