SELECT COUNT(DISTINCT Items.UserID)
FROM Items,Bids
WHERE Items.UserID == Bids.UserID;