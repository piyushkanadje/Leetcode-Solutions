class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0  # If there are 4 or fewer elements, we can make all elements the same.
        
        nums.sort()  # Sort the list to simplify finding the smallest and largest elements.
        
        # The minimum difference is the smallest among the possible 4-element differences
        return min(nums[-1] - nums[3],   # Remove the first 3 smallest elements
                   nums[-2] - nums[2],   # Remove the first 2 smallest elements and the largest element
                   nums[-3] - nums[1],   # Remove the smallest element and the first 2 largest elements
                   nums[-4] - nums[0])   # Remove the first 3 largest elements
