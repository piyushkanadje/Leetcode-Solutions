class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        

        def checkPrime(x):
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        

        bound = 0

        for i in range(len(nums)):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i-1]

            if bound <=0:
                return False

            largest = 0
            for j in range(bound-1, 1, -1):
                if checkPrime(j):
                    largest = j
                    break
            
            nums[i] = nums[i] -largest

        
        return True
