class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n ==1 :
            return True
        print(4/4)
        while n >=1:
            if n ==4 : return True
            elif n % 4 == 0 : n = n/4
            else:
                break
        return False
        
        