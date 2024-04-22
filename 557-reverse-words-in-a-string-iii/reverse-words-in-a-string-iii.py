class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)
        # words = s.split()
        # for i in range(len(words)):
        #     words[i] = words[i][::-1]

        