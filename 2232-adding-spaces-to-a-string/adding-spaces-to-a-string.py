from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        left = 0

        for right in spaces:
            result.append(s[left:right])  # Append substring
            result.append(" ")           # Append space
            left = right
        
        result.append(s[left:])          # Append the remainder of the string
        return "".join(result)           # Combine all parts efficiently
