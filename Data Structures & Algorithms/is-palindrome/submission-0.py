class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split(" ")
        s = "".join(s)
        res = ""
        for i in s:
            if i.isalnum():
                res += i
        res = res.lower()
        return res == res[::-1]
        