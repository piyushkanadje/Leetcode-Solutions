class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        count = 0
        ans = 0
        while k:
            if (happiness[count]-count) > 0:
                ans = ans + (happiness[count] - count)
                print(ans)
            count+=1
            k-=1
        
        return ans 
