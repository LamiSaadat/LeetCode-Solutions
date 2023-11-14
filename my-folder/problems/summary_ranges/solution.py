class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def formatter(array):
            if len(array) == 1: return str(array[0])
            if array[0] == array[1]: return str(array[0])
        
            el1 = str(array[0])
            el2 = str(array[1])

            return f"{el1}->{el2}"

        if len(nums) == 1: return [str(nums[0])]
        if len(nums) == 0: return
        stack = []
        results = []
        stack.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                stack.append(nums[i-1])
                results.append(formatter(stack))
                stack = [nums[i]]
        stack.append(nums[i])
        results.append(formatter(stack))
        return results
            
    
