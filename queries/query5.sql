SELECT COUNT(DISTINCT Users.UserID)
FROM Users,Items
WHERE Users.UserID == Items.UserID
AND Users.Rating > 1000;