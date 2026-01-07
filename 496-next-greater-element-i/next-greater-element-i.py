class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1=len(nums1)
        m2=len(nums2)
        res=[]
        for i in range(m1):
            max_val=-1
            is_found=False
            for j in range(m2):
                if nums1[i]==nums2[j]:
                    is_found=True
                if is_found and nums2[j]>nums1[i]:
                    max_val=nums2[j]
                    break
            res.append(max_val)
        return res

        