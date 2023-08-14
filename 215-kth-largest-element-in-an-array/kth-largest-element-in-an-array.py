import random
class Solution:
    def randomizedPartition(self,arr, low, high):
        pivotIndex = random.randint(low,high)
        arr[pivotIndex], arr[high]= arr[high], arr[pivotIndex]
        i = low -1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j]>=pivot:
                i+=1
                arr[i], arr[j]= arr[j], arr[i]
        arr[i+1], arr[high]= arr[high], arr[i+1]
        return i+1

    def randomizedSelection(self,arr, low, high, k):
        if low== high:
            return arr[low]
        pivotIndex = self.randomizedPartition(arr,low, high)
        if k == pivotIndex:
            return arr[pivotIndex]
        elif k<=pivotIndex:
            return self.randomizedSelection(arr,low, pivotIndex-1, k)
        else:
            return self.randomizedSelection(arr, pivotIndex+1, high, k)
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.randomizedSelection(nums,0,len(nums)-1,k-1)