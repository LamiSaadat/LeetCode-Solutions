class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}

        for i in range(len(s)):
            if(s[i] not in mapS):
                mapS[s[i]] = t[i]
            elif(t[i] != mapS[s[i]]):
                return False

            if(t[i] not in mapT):
                mapT[t[i]] = s[i]
            elif(s[i] != mapT[t[i]]):
                return False

        return True
                