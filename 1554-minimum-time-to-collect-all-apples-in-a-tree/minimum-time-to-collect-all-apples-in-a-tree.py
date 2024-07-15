class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        from collections import defaultdict
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        def dfs(node, parent):
            total_steps  =0
            for neighbour in adj_list[node]:
                if neighbour != parent:
                    steps = dfs(neighbour, node)
                    if steps > 0 or hasApple[neighbour]:
                        total_steps += steps + 2
            return total_steps

        return dfs(0, -1)
