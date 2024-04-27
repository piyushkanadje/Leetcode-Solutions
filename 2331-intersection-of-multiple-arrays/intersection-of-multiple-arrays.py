class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        count = collections.defaultdict(int)
        for i in nums:
            for x in i:
                count[x]+=1
        
        n= len(nums)
        for key in count.keys():
            if count[key] == n:
                ans.append(key)
        return sorted(ans)
