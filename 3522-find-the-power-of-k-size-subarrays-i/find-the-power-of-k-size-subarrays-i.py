class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        consec_count = 1
        res = []
        for i in range(len(nums)):
            if i and nums[i - 1] + 1 == nums[i]:
                consec_count += 1
            else:
                consec_count = 1

            if consec_count >= k:
                res.append(nums[i])
            elif i >= k - 1:
                res.append(-1)
                
        return res