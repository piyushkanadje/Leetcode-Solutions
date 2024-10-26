class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #What we gonna do we chose a and then a will have opitions like start +1 .... end at end i will only have single choice
        
        # We will keep a set() for to see the unique strings
        #for max value of the unique number of strings
        #i which is out starting point and set
        def dfs(i, curr_set):
          
            if i == len(s):
                return 0
            res = 0
            #We will have loop to find from start to the end like go from 1 to end
            for j in range(i,len(s)):
                substring =s[i:j+1] # Strat+1 to end so j was exclusive so we are adding it here inclusice        
                if substring in curr_set:
                    continue
                curr_set.add(substring)
                res = max(res, 1 + dfs(j+1, curr_set))
                #Why we are removing this because we want to explore other possibilit
                curr_set.remove(substring)
            return res
        
        return dfs(0, set())