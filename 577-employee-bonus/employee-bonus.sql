/* Write your T-SQL query statement below */
SELECT Employee.name , Bonus.bonus
from Employee
FULL OUTER JOIN Bonus
ON Employee.empId = Bonus.empId
Where Bonus.bonus < 1000 OR Bonus.bonus IS NULL
ORDER BY Employee.name;