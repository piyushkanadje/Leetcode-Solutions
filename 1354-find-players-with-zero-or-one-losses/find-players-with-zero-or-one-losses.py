class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        d = {}
        for match in matches:
            d[match[1]] = d.get(match[1], 0) + 1
            d[match[0]] = d.get(match[0], 0)
        #print(dlost)
        # for i in matches:
        #     if (i[0] not in dlost) and (i[0] not in notlost):
        #         notlost.append(i[0])
        #     if (i[0] in dlost) and (dlost[i[0]]==1) and (i[0] not in lost1) :
        #         lost1.append(i[0])
        #     if dlost[i[1]] == 1 and i[1] not in lost1:
        #         lost1.append(i[1])
        ans1 = []
        ans2 = []

        for key, val in d.items():
            if val == 0:
                ans1.append(key)
            if val == 1:
                ans2.append(key)
        ans1.sort()
        ans2.sort()
        return[ans1, ans2]