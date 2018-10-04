rm *.dat
python skeleton_parser.py ebay_data/items-*.json

awk '!seen[$0]++' Item.dat > Item_temp.dat
mv Item_temp.dat Item.dat

awk '!seen[$0]++' Users.dat > Users_temp.dat
mv Users_temp.dat Users.dat

awk '!seen[$0]++' Category.dat > Category_temp.dat
mv Category_temp.dat Category.dat

awk '!seen[$0]++' Bids.dat > Bids_temp.dat
mv Bids_temp.dat Bids.dat
