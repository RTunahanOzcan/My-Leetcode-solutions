SELECT id, visit_date, people
FROM Stadium s1
WHERE people >= 100
  AND (
       -- checking if current row is the middle of 3 consecutive rows
       (EXISTS (SELECT 1 FROM Stadium s2 WHERE s2.id = s1.id - 1 AND s2.people >= 100)
        AND EXISTS (SELECT 1 FROM Stadium s3 WHERE s3.id = s1.id + 1 AND s3.people >= 100))
       
       OR
       -- checking if current row is the left of 3 consecutive rows
       (EXISTS (SELECT 1 FROM Stadium s2 WHERE s2.id = s1.id + 1 AND s2.people >= 100)
        AND EXISTS (SELECT 1 FROM Stadium s3 WHERE s3.id = s1.id + 2 AND s3.people >= 100))
       
       OR
       -- checking if current row is the right of 3 consecutive rows
       (EXISTS (SELECT 1 FROM Stadium s2 WHERE s2.id = s1.id - 1 AND s2.people >= 100)
        AND EXISTS (SELECT 1 FROM Stadium s3 WHERE s3.id = s1.id - 2 AND s3.people >= 100))
      )
ORDER BY visit_date;
