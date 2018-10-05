SELECT COUNT(*)
FROM (
   SELECT ItemID
   FROM Categories
   GROUP BY ItemID
   HAVING COUNT(*) == 4);