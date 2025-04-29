class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict [sorted in in dict then add other wise create one ]
        d = {}
        for i in strs:
            sortedString = ''.join(sorted(i))
            if sortedString in d:
                d[sortedString].append(i)
            else:
                d[sortedString] = [i]
        return list(d.values())

