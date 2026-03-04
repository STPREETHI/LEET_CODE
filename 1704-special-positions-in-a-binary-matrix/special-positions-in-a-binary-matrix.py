class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                
                if mat[i][j] == 1:
                    
                    
                    if mat[i].count(1) == 1:
                        
                        
                        col_count = 0
                        for k in range(len(mat)):
                            if mat[k][j] == 1:
                                col_count += 1
                        
                        if col_count == 1:
                            count += 1
                            
        return count