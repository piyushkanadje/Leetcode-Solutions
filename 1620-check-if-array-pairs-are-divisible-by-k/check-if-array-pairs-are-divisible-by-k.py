class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d ={}

        for i in arr:
                        #we are doing i%k+k due to we want the value to be always positive and then doing %k because we want the value to be in range(0, k-1)

            d[(i%k+k)%k] = 1+ d.get((i%k+k)%k, 0) 
        
        print(d)
        for i in arr:
            rem = (i%k+k)%k
            #here we are checking all the numbers which are divisible by k
            if rem == 0:
                if d[0] % 2==1:
                    return False
            #Here we are cheking the pairs in which k-rem means lets say i = 1 and k=5 k-rem will be 4 we will need 4 in d to make 1+4==5 
            elif d[rem] != d.get(k-rem, 0):
                return False
        return True