class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        temp = []
        pointerS = 0
        pointerT = 0

        while pointerT < len(t) and pointerS < len(s):
            if t[pointerT] == s[pointerS]:
                temp.append(t[pointerT])
                pointerT+=1
                pointerS+=1
            else:
                pointerT+=1

        if "".join(temp) == "".join(s):
            return True