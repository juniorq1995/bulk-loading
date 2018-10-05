<<<<<<< HEAD
WITH temp AS (
   SELECT COUNT(ItemID)
   FROM Categories
   GROUP BY ItemID
   HAVING COUNT(*) == 4)

SELECT COUNT(*)
FROM temp;
=======
SELECT COUNT(*)
FROM Categories
>>>>>>> 5f2d491bd4d6607b07f547637df8984f58edc551
