class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        completeTime = customers[0][0] + customers[0][1]
        waitingTime = completeTime - customers[0][0]

        for i in range(1,len(customers)):
            if customers[i][0] <= completeTime:
                completeTime+=customers[i][1]
            else:
                completeTime = customers[i][0] + customers[i][1]
            waitingTime += (completeTime - customers[i][0])
        
        return waitingTime/len(customers)

        
    
