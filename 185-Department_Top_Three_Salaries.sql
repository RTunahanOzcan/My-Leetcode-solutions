SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
FROM (
    SELECT e.*,
           DENSE_RANK() OVER (
               PARTITION BY e.departmentId   -- Restart ranking for each department
               ORDER BY e.salary DESC        -- Rank salaries from highest to lowest
           ) AS rnk
    FROM Employee e
) e
JOIN Department d
  ON e.departmentId = d.id          -- Match employee’s department
WHERE e.rnk <= 3;                   -- Keep only employees in top 3 unique salaries
