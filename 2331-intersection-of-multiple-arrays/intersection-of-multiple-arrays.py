class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = collections.defaultdict(int)
        for i in nums:
            for j in i:
                d[j]+=1
        ans =[]
        for j in d.keys():
            if d[j] == len(nums):
                ans.append(j)

        return sorted(ans)