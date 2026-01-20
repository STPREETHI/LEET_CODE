SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id=e2.managerID
Where e1.salary<e2.salary
