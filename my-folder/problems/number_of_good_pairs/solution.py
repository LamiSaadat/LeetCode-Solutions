from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #input - list
        #output - num

        tracker = {}
        result = 0

        for num in nums:
            if num in tracker:
                result += tracker[num]
                tracker[num] += 1
            else:
                tracker[num] = 1
        return result


