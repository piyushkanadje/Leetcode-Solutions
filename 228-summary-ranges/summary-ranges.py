class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0:
            return[]
        if len(nums) ==1:
            return [str(nums[0])]

        first = nums[0]
        ans = []

        for i in range(1, len(nums)):
            if nums[i]== nums[i-1]+1:
                continue
            
            if first == nums[i-1]:
                ans.append(str(nums[i-1]))
            else:
                ans.append(f"{first}->{nums[i-1]}")
            first= nums[i]
        
                # Add the last range after the loop
        if first == nums[-1]:
            ans.append(str(first))
        else:
            ans.append(f"{first}->{nums[-1]}")

        return ans
            
