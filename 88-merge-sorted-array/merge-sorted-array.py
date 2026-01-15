class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        i = m - 1       # last valid element in arr1
        j = n - 1       # last element in arr2
        k = m + n - 1   # last index in arr1

        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1

        # If any elements left in arr2
        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1
