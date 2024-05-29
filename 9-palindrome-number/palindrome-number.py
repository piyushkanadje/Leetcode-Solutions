class Solution:
    def isPalindrome(self, x: int) -> bool:
        newNumber = 0
        remainder = 0
        original = x
        if x < 0:
            return False
        while x:
            lastDigit = x % 10
            newNumber = newNumber * 10 + lastDigit
            x = x//10
        print(newNumber)
        if original == newNumber:
            return True
        else: 
            return False
