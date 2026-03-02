class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[[]]
        for num in nums:
                res+=[curr + [num] for curr in res]
         # convert to tuples to make hashable
        res = set(tuple(x) for x in res)
        
        # convert back to list of lists
        return [list(x) for x in res]
            
        