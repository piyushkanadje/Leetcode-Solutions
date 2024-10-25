class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        sorted_folder = sorted(folder, key=len)
        print(sorted_folder)
        res = set()
        for i in sorted_folder:
            f = i[1:].split('/')
            curr =''
            for i in range(len(f)):
                curr = curr+ '/'+ f[i]
                if curr in res:
                    break
                if i== len(f)-1:
                    res.add(curr)
        return list(res)

                                                                                              