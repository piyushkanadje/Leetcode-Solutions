import random

class Solution:

    def partition(self, arr, low, high):
        x = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= x:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i 

    def kthSmallest(self, arr, low, high, k):
        if k > 0 and k <= high - low + 1:
            index = self.partition(arr, low, high)
            if index - low == k - 1:
                return arr[index]
            if index - low > k - 1:
                return self.kthSmallest(arr, low, index - 1, k)
            return self.kthSmallest(arr, index + 1, high, k - index + low - 1)

    def findKthLargest(self, nums, k):
        return self.kthSmallest(nums, 0, len(nums) - 1, len(nums) - k + 1)


