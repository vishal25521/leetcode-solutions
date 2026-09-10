# Write your MySQL query statement below
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
join Department d
    ON e.departmentId = d.id
WHERE (
    SELECT count(DISTINCT e2.salary)
    from Employee e2
    WHERE e2.departmentId = e.departmentId
      AND e2.salary > e.salary
) < 3; 