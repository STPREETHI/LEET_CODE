class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        nums.reverse()
        first_part=nums[:k]
        first_part.reverse()
        second_part=nums[k:]
        second_part.reverse()
        nums[:]=first_part+second_part
        return nums
        