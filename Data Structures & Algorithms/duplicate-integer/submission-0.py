class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i,0) + 1
        for i,j in hmap.items():
            if j > 1:
                return True
        return False
        