class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:          # repeat until single digit
            sum1 = 0
            num1 = str(num)
            for i in num1:
                sum1 += int(i)
            num = sum1            # update num for next iteration
        return num
