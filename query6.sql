SELECT COUNT(*)
FROM Items, Bids
WHERE Items.UserID == Bids.UserID
GROUP BY Items.UserID AND Bids.UserID