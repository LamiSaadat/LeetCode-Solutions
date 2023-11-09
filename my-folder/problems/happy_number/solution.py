from collections import defaultdict
class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1: return True

        hash = defaultdict()
        newN = n

        while newN != 1:
            newN = reduce(lambda a, b: a + b, [int(num) * int(num) for num in [*str(newN)]])
            if newN in hash:
                return False
            else:
                hash[newN] = newN
        return True