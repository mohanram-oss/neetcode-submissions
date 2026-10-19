class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        arr = []
        for i in strs:
            word = "".join(sorted(i))
            if word in output:
                output[word].append(i)
            else:
                output[word] = [i]
        for i,j in output.items():
            arr.append(j)

        return arr

        