class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = [0]* (len(gain)+1)
        for i in range(len(gain)):
            prefixSum[i] = prefixSum[i-1]+ gain[i]
        
        return max(prefixSum)