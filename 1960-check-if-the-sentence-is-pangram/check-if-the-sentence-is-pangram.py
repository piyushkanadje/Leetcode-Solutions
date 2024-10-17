        
        
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for i in range(len(sentence)):
            s.add(sentence[i])
            
        return True if len(s) == 26 else False