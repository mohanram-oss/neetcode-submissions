class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        freq_t = {}
        for i in s:
            freq_s[i] = freq_s.get(i,0) + 1
        for j in t:
            freq_t[j] = freq_t.get(j,0) + 1 
        for key, val in freq_s.items():
            if val != freq_t.get(key,0):
                return False
        return True