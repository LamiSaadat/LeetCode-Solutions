from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = Counter(arr)

        if len(map.values()) == len(set(map.values())):
            return True