class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        maxx =0 

        def helper(i, curr):
            nonlocal count , maxx
            if i == len(nums):
                return
            
            if curr | nums[i] > maxx:
                maxx = curr | nums[i]
                count = 1
            
            elif curr | nums[i] == maxx:
                count += 1
            #include this nums[i] in bitwise or 
            helper(i+1, curr|nums[i])
            #do not include this nums[i] in bitwise or
            helper(i+1, curr)
            
        
        helper(0,0)

        return count