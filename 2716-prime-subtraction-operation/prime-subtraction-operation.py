class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        

        def checkPrime(x):
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        maxElement =max(nums)
        bound = 0
        previous_prime = [0] * (maxElement + 1)
        for i in range(2, maxElement + 1):
            if checkPrime(i):
                previous_prime[i] = i
            else:
                previous_prime[i] = previous_prime[i - 1]
        for i in range(len(nums)):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i-1]

            if bound <=0:
                return False

            largest = previous_prime[bound-1]
   
            
            nums[i] = nums[i] -largest

        
        return True
