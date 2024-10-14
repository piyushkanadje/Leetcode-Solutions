class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        # Sort and remove duplicates
        nums = sorted(set(nums))
        summ, current = 0, 1
        
        for num in nums:
            if num > current:
                count = min(k, num - current)
                summ += (current + current + count - 1) * count // 2
                k -= count
                if k == 0:
                    return summ
            current = num + 1
        
        # If k still remains, add the remaining terms
        if k > 0:
            summ += (current + current + k - 1) * k // 2
        
        return summ
