class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        d2 = Counter(s2[:len(s1)-1])
        left = 0
        for right in range(len(s1)- 1 , len(s2)):
            d2[s2[right]] +=1
            if d1 == d2:
                return True
            
            d2[s2[left]]-=1
            if d2[s2[left]] == 0:
                del d2[s2[left]]

            left+=1
        return False

