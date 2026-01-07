class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even =[x for x in nums if x%2==0]
        odd =[x for x in nums if x%2!=0]
        nums[::2]=even
        nums[1::2]=odd
        return nums
        