class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=0
        for i in range(n):
            curr_min=nums[i]
            curr_max=nums[i]
            for j in range(i,n):
                curr_min=min(nums[j],curr_min)
                curr_max=max(nums[j],curr_max)
                total_sum+=curr_max-curr_min
        return total_sum
        