class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        arr = [0] * 26
        for i in range(len(sentence)):
            arr[ord(sentence[i]) - ord('a')]=1
        print(arr)
        return True if sum(arr) == 26 else False