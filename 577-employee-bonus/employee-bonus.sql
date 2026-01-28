select name,bonus from Employee
left join bonus on Employee.empId=Bonus.empId
WHERE Bonus<1000 or Bonus IS NULL;