class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d ={}
        for i in range(len(nums)):
            if nums[i] in d  and abs(d.get(nums[i]) - i)<=k:
                return True
            
            d[nums[i]]= i
        
        return False