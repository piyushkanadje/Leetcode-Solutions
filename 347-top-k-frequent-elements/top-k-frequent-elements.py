class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sortedCount = sorted(count.items() , key = lambda x:x[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(sortedCount[i][0])
        return ans