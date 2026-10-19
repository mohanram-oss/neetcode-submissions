class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(numbers)):
            res = target - numbers[i]
            if res not in hmap:
                hmap[numbers[i]] = i + 1
            else:
                return [hmap[res],i+1]

        