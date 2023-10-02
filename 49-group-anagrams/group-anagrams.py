class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            sortedString = ''.join(sorted(i))
            if sortedString not in dict:
                dict[sortedString] = [i]
            else:
                dict[sortedString].append(i)
        
        return dict.values()


            