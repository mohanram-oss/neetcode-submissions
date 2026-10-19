class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}
        for i in s:
            smap[i] = smap.get(i,0) + 1
        for j in t:
            tmap[j] = tmap.get(j,0) + 1   
        for i,j in smap.items():
            if j != tmap.get(i,0):
                return False
        return True     