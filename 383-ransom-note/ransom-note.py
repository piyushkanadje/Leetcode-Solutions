class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_counter= Counter(ransomNote)
        magzine_counter= Counter(magazine)
        for i in ransomNote:
            if i not in magzine_counter:
                return False
            
            if i in magzine_counter and magzine_counter[i] < ransomNote_counter[i]:
                return False
        
        return True