class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        letter = set()
        right = 0

        while right < len(s):
            if s[right] not in letter:
                letter.add(s[right])
                right+=1
                ans = max(ans, len(letter))
            else:
                letter.remove(s[left])
                left+=1

        return ans
