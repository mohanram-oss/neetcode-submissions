class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        max_arr = [[] for i in range(len(nums) + 1)]
        for i in nums:
            hmap[i] = hmap.get(i,0) + 1
        for i,j in hmap.items():
            max_arr[j].append(i)
        res = []
        for i in range(len(max_arr)-1,0,-1):
            for j in max_arr[i]:
                res.append(j)
                if len(res) == k:
                    return res


        


        