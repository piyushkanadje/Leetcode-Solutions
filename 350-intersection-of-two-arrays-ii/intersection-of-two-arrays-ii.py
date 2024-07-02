class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        htab1 ={}
        htab2 = collections.defaultdict(int)
        ans =[]
        for i in range(len(nums1)):
            htab1[nums1[i]]=1+ htab1.get(nums1[i],0)
        
        for i in nums2:
            htab2[i]+=1
        
        for i in nums1:
            if i in nums2 and i in htab2:
                ans.append(i)
                htab2[i]-=1
                if htab2[i]==0:
                    del(htab2[i])
        return ans