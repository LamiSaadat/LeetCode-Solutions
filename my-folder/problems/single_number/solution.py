class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsMap = defaultdict(lambda: 0)

        for num in nums:
            numsMap[num] += 1
        
        for num in numsMap:
            if numsMap[num] == 1:
                return num