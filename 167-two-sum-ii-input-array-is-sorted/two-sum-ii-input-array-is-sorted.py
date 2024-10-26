class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        summ  = 0 

        while l < r:
            summ = numbers[l] + numbers[r]
            if summ== target:
                return [l+1, r+1]
            elif summ > target:
                summ-=numbers[r]
                r-=1
            else:
                summ-=numbers[l]
                l+=1
        
        