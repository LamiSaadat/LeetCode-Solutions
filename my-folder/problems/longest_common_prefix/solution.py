class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prefix = ""
        while strs[0][i]:
            for word in strs:
                if (word[i] == strs[0][i]):
                    prefix += word[i]
            i+=1
        return prefix