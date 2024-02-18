class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary(nums,l,r,target):
            mid = (l+r)//2
            if l>=r or mid ==l or mid ==r:
            
                if target==nums[mid]:
                    return mid
                elif target > nums[mid]:
                    return mid+1
                else:
                    if mid-1<0:
                        return 0
                    else:
                        return mid-1
            
            op = 0
            if nums[mid] == target:
                return mid
            if target> nums[mid]:
                op = binary(nums,mid,r, target)
            else:
                op = binary(nums,l,mid, target)
            return op

        return binary(nums,0,len(nums), target)
            
        