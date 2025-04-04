# Write your MySQL query statement below

SELECT e.name as Employee FROM Employee e
INNER JOIN Employee m on m.id = e.managerID
WHERE e.Salary> m.Salary;
