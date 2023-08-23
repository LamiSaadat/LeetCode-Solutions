class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0

        for i in range(len(nums)):
            if i == 0:
                left = 0
            else: 
                left = sum(nums[slice(0, i)])

            if i == len(nums)-1:
                right = 0
            else:
                right = sum(nums[slice(i+1, len(nums))])

            if left == right:
                return i
        return -1




            

