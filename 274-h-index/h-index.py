class Solution:
    def hIndex(self, citations: List[int]) -> int:

        #think like a geometry graph with on x axis number of paper and y axis number of citations
        #Then the max number of citation==paper is answer
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0