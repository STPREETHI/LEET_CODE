class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for key,values in h.items():
            if values>1:
                return True
        return False