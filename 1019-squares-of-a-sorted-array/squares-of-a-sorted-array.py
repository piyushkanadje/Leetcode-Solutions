class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i , j = 0 , len(nums)-1
        square = []

        while i <=j:
            if abs(nums[i]) >nums[j]:
                square.append(nums[i]**2)
                i+=1
            else:
                square.append(nums[j]**2)
                j-=1
        
        return square[::-1]

                