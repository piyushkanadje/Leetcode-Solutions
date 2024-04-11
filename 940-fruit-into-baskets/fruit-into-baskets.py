class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        curr  = 0
        fruitsCount = 0
        left = 0
        ans = 0
        fruit = {}
        curr = 0

        for right in range(len(fruits)):
            fruit[fruits[right]] =1  + fruit.get(fruits[right], 0 )
            while len(fruit) > 2:
                fruit[fruits[left]] -= 1
                if fruit[fruits[left]] == 0:
                    del fruit[fruits[left]]  # Remove the fruit if its count is 0
                left += 1
            ans = max(ans, right- left +1 )
        return ans
                




            
