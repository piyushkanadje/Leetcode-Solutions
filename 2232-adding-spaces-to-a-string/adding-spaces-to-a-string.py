class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_string = ""
        left=0
        spaces.sort()
        for right in spaces:
            if right == 0:
                new_string= new_string + " "
                left = right
                continue
            
            new_string= new_string+ " " +  s[left:right]
            left = right
        new_string = new_string + " " + s[left:]
        return new_string[1:]