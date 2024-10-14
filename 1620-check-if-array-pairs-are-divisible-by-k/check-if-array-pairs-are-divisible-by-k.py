class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = defaultdict()
        for i in arr:
            #we are doing i%k+k due to we want the value to be always positive and then doing %k because we want the value to be in range(0, k-1)
            d[(i%k+k)%k]= d.get((i%k+k)%k,0) + 1
        
        for i in arr:
            rem = (i%k+k)%k

            if rem == 0:
                if d[0] % 2==1:
                    return False
            
            elif d[rem] != d.get(k-rem, 0):
                return False
        return True