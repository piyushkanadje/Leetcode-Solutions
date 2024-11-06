class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        num_of_set= bin(nums[0]).count("1")
        min_of_seg=nums[0]
        max_of_seg=nums[0]

        max_pre=float("-inf")

        for i in range(1,len(nums)):
            if num_of_set == bin(nums[i]).count("1"):
                max_of_seg= max(max_of_seg, nums[i])
                min_of_seg= min(min_of_seg, nums[i])

            else:
                if min_of_seg < max_pre:
                    return False
                
                max_pre = max_of_seg

                max_of_seg=nums[i]
                min_of_seg = nums[i]
                num_of_set= bin(nums[i]).count("1")
        
        if min_of_seg < max_pre:
            return False
        
        return True