rm -f *.dat
python skeleton_parser.py ebay_data/items-*.json
awk '!seen[$0]++' Items.dat > Items_temp.dat
awk '!seen[$0]++' Users.dat > Users_temp.dat
awk '!seen[$0]++' Categories.dat > Categories_temp.dat
awk '!seen[$0]++' Bids.dat > Bids_temp.dat
mv Items_temp.dat Items.dat
mv Users_temp.dat Users.dat
mv Categories_temp.dat Categories.dat
mv Bids_temp.dat Bids.dat
