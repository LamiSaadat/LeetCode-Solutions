class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_pairs = {}
        for index, num in enumerate(nums):
            if target - num in num_index_pairs:
                return [num_index_pairs[target - num], index]
            else:
                num_index_pairs[num] = index