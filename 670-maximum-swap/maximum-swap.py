class Solution:
    def maximumSwap(self, num: int) -> int:
        n = str(num)

        #dict to store the position of the element
        d = dict()
        arr = []
        for i in range(len(n)):
            if n[i] in d:
                d[n[i]].append(i)
            else:
                d[n[i]] = [i]
            
            arr.append(int(n[i]))
        arr1 = sorted(arr, reverse = True)
        # now we need to find the swap positions
        swap1 = 0
        swap2 = 0

        for i in range(len(n)):
            if int(n[i]) != arr1[i]:
                swap1 = i
                swap2 = d[str(arr1[i])][-1]
                break
        
        tmp = arr[swap1]
        arr[swap1] = arr[swap2]
        arr[swap2] = tmp

        ans = ""
        for i in arr:
            ans +=str(i)

        
        return int(ans)