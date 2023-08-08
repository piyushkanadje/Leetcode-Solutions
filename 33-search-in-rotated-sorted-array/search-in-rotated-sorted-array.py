class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        fix  = nums[0]

        if target < fix :
            right =  len(nums) - 1

            while True:
                if right >=0 and nums[right] == target:
                    return right
                if right < 0 or target > nums[right]:
                    return -1
                right -=1
        elif target >fix :
            left =0 

            while True:
                if left <= len(nums)-1 and  nums[left] == target:
                    return left
                if left > len(nums)-1 or nums[left] > target:
                    return -1

                left+=1
        else: 
            if target == fix:
                return 0
        return -1


        