SELECT COUNT(DISTINCT Categories.Category)
FROM Categories,Bids
WHERE Categories.ItemID == Bids.ItemID
AND CAST(Bids.Amount AS DOUBLE) > 100;