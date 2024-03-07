class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = deque(sentence1.split(' '))
        s2 = deque(sentence2.split(' '))

        while s1 and s2:
            if s2[0] == s1[0]:
                s2.popleft()
                s1.popleft()
                continue
            elif s2[-1] == s1[-1]:
                s2.pop()
                s1.pop()
                continue
            return False
        return True