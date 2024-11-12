class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        sorted_items= sorted(items, key = lambda x: x[0])
        ans = [0] * len(queries)

        queries_with_index = [[queries[i],i] for i in range(len(queries))]
        queries_with_index.sort(key= lambda x:x[0])
        maxxBeauty = 0
        item_index = 0
        for i in range(len(queries_with_index)):

            while item_index < len(sorted_items) and sorted_items[item_index][0] <= queries_with_index[i][0]:
                maxxBeauty = max(maxxBeauty, sorted_items[item_index][1])
                item_index+=1

            ans[queries_with_index[i][1]] = maxxBeauty
        return ans


