class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length = min(len(nums1), len(nums2))
        ans = set()
        for i in range(length):
            if (nums1[i] in nums2):
                ans.add(nums1[i])
            if (nums2[i] in nums1):
                ans.add(nums2[i])
        return ans