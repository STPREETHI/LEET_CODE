class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # Overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        if dividend == divisor:
            return 1
        
        elif dividend == -divisor:
            return -1
        
        elif divisor == 1:
            return dividend
        
        elif divisor == -1:
            return -dividend
        
        else:
            result = int(dividend / divisor)
            return result
