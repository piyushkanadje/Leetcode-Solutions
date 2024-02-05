class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
            length = 0
            maxNum = float('-inf')
            maxAns = float('-inf')
            for j in range(i, min(n, i + k)):
                length += 1
                maxNum = max(maxNum, arr[j])
                summ = length * maxNum + dp[j+1]
                maxAns = max(maxAns, summ)
            dp[i] = maxAns

        return dp[0]