class Solution:
    def maximumSwap(self, num: int) -> int:
        nums  = list(str(num))
        max_i = -1
        max_digit = "0"
        swapi, swapj= -1,-1
        for i in reversed(range(len(nums))):
            #Find the max
            if nums[i] > max_digit:
                max_digit = nums[i]
                max_i = i

            if nums[i] < max_digit: 
                swapi, swapj= max_i, i

        nums[swapi], nums[swapj] = nums[swapj], nums[swapi]

        return int("".join(nums))
