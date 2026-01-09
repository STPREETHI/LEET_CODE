from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        return list(combinations(nums,k))
        