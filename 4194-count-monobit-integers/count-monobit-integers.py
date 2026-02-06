class Solution:
    def countMonobit(self, n: int) -> int:
        count1=0
        arr1=[]
        for i in range(0,n+1):
            arr1.append(bin(i)[2:])
        print(arr1)
        for i in arr1:
            if len(set(i))==1:
                count1+=1
        return count1
                
                
            
        