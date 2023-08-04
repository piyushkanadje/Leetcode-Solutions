class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        #Curr will have all out combination and then we will copy the combination and put it into out res
        curr =[]
        #As we know backtrack is all about the recursion 
        def dfs(i, curr, total):
            # here we have defined the fucntion dfs where our decision tree will have i in it and we will have i and in other branch we will not have i

            #when ever the total is equal to target means we got out combination
            if total == target:
                res.append(curr.copy())
                return
            if i>=len(candidates) or total > target:
                return
            
            #Here we are add the candidate and incrementing the total
            curr.append(candidates[i])
            dfs(i,curr, total+candidates[i])

            # here we are removing the candidate[i] and adding the next one
            curr.pop()
            dfs(i+1, curr,total )

        
        dfs(0,[],0)
        return res