class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        out = []
        for i in range(1,len(nums),1):
            prod = nums[i-1] * prefix[i-1]
            prefix[i] = prod
        for j in range(len(nums)-2,-1,-1):
            prod = nums[j+1] * suffix[j+1]
            suffix[j] = prod
        for i in range(len(nums)):
            out.append(prefix[i]*suffix[i])
        return out


        
        