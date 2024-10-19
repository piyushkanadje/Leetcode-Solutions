class Solution:

    def invertAndReversed(self,s):
        ans=""
        for i in s:
            if int(i)==0:
                ans+="1"
            else:
                ans+="0"
        return ans[::-1]

    def findKthBit(self, n: int, k: int) -> str:
        
        S1="0"
        arr = [0] * (n+1)
        arr[0] = S1
        for i in range(1, n+1):
            arr[i] = arr[i-1] + "1" + self.invertAndReversed(arr[i-1])
        
        return arr[n][k-1]