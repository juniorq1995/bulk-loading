SELECT COUNT(*)
FROM Users U
GROUP BY U.UserID
HAVING U.Location == "New York";