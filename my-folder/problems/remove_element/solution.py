class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                nums[i] = 0
        nums.sort(reverse=True)
        k = len(nums)-count
        return k

