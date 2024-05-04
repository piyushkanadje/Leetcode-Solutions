class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for i in range(len(paths)):
            print(paths[i][0])
            d[paths[i][0]] = 1 + d.get(paths[i][0], 0)
        print(d)
        for i in range(len(paths)):
            if paths[i][1] not in d:
                return paths[i][1]