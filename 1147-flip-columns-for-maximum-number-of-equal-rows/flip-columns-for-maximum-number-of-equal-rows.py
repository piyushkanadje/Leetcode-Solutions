class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        d = {}

        for row in matrix:
            z_list = list()
            o_list = list()
            for i in range(len(row)):
                if row[i] == 0:
                    z_list.append(i)
                
                else:
                    o_list.append(i)
            t_z = tuple(z_list)
            t_o = tuple(o_list)

            d[t_z] = d.get(t_z, 0) + 1
            d[t_o] = d.get(t_o, 0) + 1
        
  
        return max(list(d.values()))
