from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        desq = deque()
        insq = deque()

        ans = 0
        left =0
        for right , num in enumerate(nums):
            while desq and num > desq[-1]:
                desq.pop()
            desq.append(num)

            while insq and num < insq[-1]:
                insq.pop()
            insq.append(num)

            while desq[0] - insq[0] > limit:
                if desq[0] == nums[left]:
                    desq.popleft()
                if insq[0] == nums[left]:
                    insq.popleft()
                
                left+=1

            ans = max(ans, right - left +1)
        
        return ans