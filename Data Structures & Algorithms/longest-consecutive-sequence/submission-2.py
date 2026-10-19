class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_cnt = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                count = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    count += 1
                max_cnt = max(max_cnt, count)
        return max_cnt
