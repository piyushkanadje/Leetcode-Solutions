class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subsets = []
        def dfs(index):
            if index >=len(nums):
                res.append(subsets.copy())
                print(res)
                return
            #Decision to include the nums[i]
            subsets.append(nums[index])
            dfs(index+ 1)      
            #Decision to exclude nums[o]
            subsets.pop()
            dfs(index+1)
        dfs(0)
        return res
    