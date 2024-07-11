from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = 0
        for log in logs:
            if log == "../":
                if operations > 0:
                    operations -= 1
            elif log != "./":
                operations += 1
        
        return operations
