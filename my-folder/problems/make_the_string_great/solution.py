class Solution:
    def makeGood(self, s: str) -> str:
        good = []

        for i in range(len(s)):
            if good and good[-1] == s[i].swapcase():
                good.pop()
            else:
                good.append(s[i])
            print(good)

        return ''.join(good)

