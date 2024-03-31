class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        totalNumber = m + n -1

        while pointer2 >=0:
            if pointer1>=0 and nums1[pointer1] > nums2[pointer2]:
                nums1[totalNumber] = nums1[pointer1]
                totalNumber-=1
                pointer1-=1
            else:
                nums1[totalNumber] = nums2[pointer2]
                pointer2-=1
                totalNumber-=1
