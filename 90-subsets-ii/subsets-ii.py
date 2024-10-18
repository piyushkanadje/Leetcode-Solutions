

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the input to make duplicates adjacent
        subset = []

        def dfs(i):
            if i == len(nums):
                # Add subset to res only if it's not already present
                if subset not in res:
                    res.append(subset.copy())
                return
            
            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude nums[i] and backtrack
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
