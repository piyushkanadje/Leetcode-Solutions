

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the input to make duplicates adjacent
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude nums[i] and backtrack
            subset.pop()
            #Do not add duplicates
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i + 1)
        
        dfs(0)
        return res
