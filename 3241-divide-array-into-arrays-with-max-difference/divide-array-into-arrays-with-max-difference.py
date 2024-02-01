class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    
        if len(nums) % 3 !=0:
            return []
        
        ans = []
        nums.sort()
        for i in range(0, len(nums), 3):
            if i + 2 < len(nums) and nums[i+2] - nums[i] <=k:
                ans.append([nums[i], nums[i+1], nums[i+2]])
            else:
                return []
        
        return ans

