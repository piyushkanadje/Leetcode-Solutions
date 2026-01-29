class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for i in range(len(sentence)):
            d[sentence[i]] = 1
        if len(d)!= 26:
            return False
        print(d.items())
        return True