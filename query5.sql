SELECT COUNT(*)
FROM Users, Items
WHERE Users.UserID == Items.UserID AND 
      Users.Rating > 1000
GROUP BY Users.UserID AND Items.UserID