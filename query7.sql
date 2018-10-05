SELECT COUNT(*)
FROM Categories, Items, Bids
WHERE Items.Category == Categories.Category 
	AND Items.ItemID == Bids.ItemID
	AND Bids.Amount > 100
GROUP BY Categories.Category