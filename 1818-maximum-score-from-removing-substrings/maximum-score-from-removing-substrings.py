class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score =0
        highest_priority = "ab" if x > y else "ba"
        lowest_priority = "ba" if highest_priority == "ab" else "ab"
        
        string_after_highest = self.remove_string(s, highest_priority)
        total_score += ((len(s) - len(string_after_highest))//2) * max(x,y)

        string_after_lowest = self.remove_string(string_after_highest, lowest_priority)
        total_score +=((len(string_after_highest)- len(string_after_lowest))//2)* min(x,y)
    
        return total_score

    def remove_string(self,input: str , target: str):
        stack = []

        for char in input:
            if stack and stack[-1]== target[0] and char ==target[1]:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)

        