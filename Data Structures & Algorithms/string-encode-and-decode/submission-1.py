class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for i in strs:
            arr.append(str(len(i)))
            arr.append("#")
            arr.append(i)
        return "".join(arr)



    def decode(self, s: str) -> List[str]:

        output = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            output.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return output