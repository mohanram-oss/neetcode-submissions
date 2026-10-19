class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        for num, val in freq.items():
            if val > 1:
                return True
        return False
        