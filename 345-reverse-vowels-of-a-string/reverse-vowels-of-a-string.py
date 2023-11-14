class Solution:
    def reverseVowels(self, s: str) -> str:
        low= 0
        high =len(s) -1
        vowels = "aeiouAEIOU"
        sli = list(s)
        while low < high:
            if sli[low] in vowels and sli[high] in vowels:
                sli[low], sli[high] = sli[high], sli[low]
                low += 1
                high -= 1
            if sli[low] not in vowels:
                low += 1
            if sli[high] not in vowels:
                high -= 1

        return "".join(sli)
        

