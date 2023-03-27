class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newSet = set()

        for num in range(len(nums)):
            if nums[num] not in newSet:
                newSet.add(nums[num])
            else:
                return True

        return False