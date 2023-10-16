from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = defaultdict()
        s = s.split()

        if len(pattern) != len(s):
            return False
        if (len(set(pattern))) != len(set(s)):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in map:
                 map[pattern[i]] = s[i]
            elif map[pattern[i]] != s[i]:
                return False
        return True