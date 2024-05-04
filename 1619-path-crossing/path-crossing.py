class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        s.add((0,0))
        t = [0,0]
        for d in path:
            if d == "N":
                t[0] += 1
            elif d == "S":
                t[0] -= 1
            elif d == "E":
                t[1] += 1
            else:
                t[1] -= 1
            if tuple(t) in s:
                return True
            s.add(tuple(t))
        return False