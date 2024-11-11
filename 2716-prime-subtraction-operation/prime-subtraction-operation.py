class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        # We only have to check until its sq root because divisors came in pair like for 36 divisors are 2,18 3,12 6,6 
        def checkPrime(x):
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        maxElement =max(nums)
        bound = 0
        #Here we are storinf prime number less than the max Element in the nums
        previous_prime = [0] * (maxElement + 1)
        for i in range(2, maxElement + 1):
            if checkPrime(i):
                previous_prime[i] = i
            else:
                previous_prime[i] = previous_prime[i - 1]

        #here bound will be necessary at each index we need to subtract the optimal prime number 
        # 1- largest prime number which is less than the current number and its nums[i] - largest prime must be greator than nums[i-1] so nums[i] -nums[i-1] == bound and we need to find less than bound
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
