class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a' , 'e', 'i', 'o', 'u']

        l = 0
        r = len(s) - 1

        s = list(s)

        while (l < r):
            if s[l].lower() not in vowels:
                l+=1
            elif s[r].lower() not in vowels:
                r-=1
            else:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
        return "".join(s)