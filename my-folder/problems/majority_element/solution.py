from collections import defaultdict 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums)/2
        map = defaultdict(lambda: 0)

        for i in range(len(nums)):
            map[nums[i]] += 1

        for key, value in map.items():
            if value > threshold:
                return key