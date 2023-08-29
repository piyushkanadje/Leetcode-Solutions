class Solution:
    def bestClosingTime(self, customers: str) -> int:
        maxScore = score = 0
        best_hour = -1
        for i , c in enumerate(customers):
            score += 1 if c == 'Y' else -1            
            if score > maxScore:
                maxScore , best_hour = score ,i
            
        return best_hour + 1
        


            