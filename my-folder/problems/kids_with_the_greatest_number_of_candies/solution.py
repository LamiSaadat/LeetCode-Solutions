class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in range(len(candies)):
            currKidCandies = candies[i] + extraCandies
            maxInCandies = max(candies)
            if currKidCandies >= maxInCandies:
                result.append(True)
            else:
                result.append(False)
        return result