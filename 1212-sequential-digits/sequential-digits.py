class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        for i in range(1,10):
            num = i
            next_nums = i + 1

            while num <= high and next_nums<=9:
                num  = num * 10 + next_nums
                if low <= num <= high:
                    ans.append(num)
                next_nums +=1
        ans.sort()
        return ans
