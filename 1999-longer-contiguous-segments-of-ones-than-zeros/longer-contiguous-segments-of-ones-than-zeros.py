class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max1=max(len(x) for x in s.split('0'))
        max2=max(len(x) for x in s.split('1'))
        return max1>max2
        

        
            


        