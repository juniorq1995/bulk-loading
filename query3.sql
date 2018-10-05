WITH temp AS (
   SELECT COUNT(ItemID)
   FROM Categories
   GROUP BY ItemID
   HAVING COUNT(*) == 4)

SELECT COUNT(*)
FROM temp;