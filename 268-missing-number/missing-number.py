class Solution:
    def sum_of_n(self, n):
        return n * (n + 1) // 2
    def missingNumber(self, nums: List[int]) -> int:
        
        return self.sum_of_n(len(nums)) - sum(nums)