class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * n
        def dfs(arr, k, index,dp):
            if index == n:
                return 0
            if dp[index] != -1: return dp[index]
            length = 0
            maxNum = float('-inf')
            maxAns = float('-inf')
            for i in range(index, min(n, index + k)):
                length += 1
                maxNum = max(maxNum, arr[i])
                summ = length * maxNum + dfs(arr, k, index + length,dp)
                maxAns = max(maxAns, summ)
            dp[index] = maxAns
            return dp[index]
        return dfs(arr ,  k , 0, dp)