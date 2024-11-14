class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(k):
            stores = 0
            for q in quantities:
                stores+=ceil(q/k)

            return stores <= n
        
        if len(quantities)==1:
            return max(quantities)
        low= 1
        high = max(quantities)

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                high =mid - 1
            else:
                low = mid + 1
        
        return low