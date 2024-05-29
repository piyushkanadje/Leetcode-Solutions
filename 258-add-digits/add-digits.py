class Solution:
    def addDigits(self, n: int) -> int:
        sum = 0

        while n :
            sum+=(n%10)
            n = (n//10)
            if n ==0 and sum < 10:
                return sum
            elif n==0 and sum >=10:
                n= sum
                sum = 0
        return sum