
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub
import os

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json'!git file
        # open files to hold each tables data
        categoryDataFile = open("Categories.dat","a")
        itemDataFile = open("Items.dat","a")
        bidsDataFile = open("Bids.dat", "a")
        userDataFile = open("Users.dat", "a")

        # iterate through all JSON objects
        for item in items:
            """
            Create Item table
            """
            # Check if description value is empty, if not fill var with value
            description = "NULL"
            if item["Description"] != None:
                description = item["Description"]
            itemDataFile.write("\"" + item['ItemID'] + "\"|\"" + sub("\"","\"\"",item['Seller']['UserID']) + "\"|\"" + sub("\"","\"\"",(item['Name'])) + "\"|\"" + sub("\"","\"\"",transformDollar(item['Currently'])) + "\"|\"" + sub("\"","\"\"",transformDollar(item['First_Bid'])) + "\"|" + item['Number_of_Bids'] + "|\"" + sub("\"","\"\"",item['Location']) + "\"|\"" + sub("\"","\"\"",item['Country']) + "\"|\"" + sub("\"","\"\"",transformDttm(item['Started'])) + "\"|\"" + sub("\"","\"\"",transformDttm(item['Ends'])) + "\"|\"" + sub("\"","\"\"",description) + "\"\n")

            """
            Create Categories table
            """
            # Create Categories table
            for category in item['Category']:
                 #write to file using same format
                categoryDataFile.write("\"" + sub("\"","\"\"",category) + "\"|\"" + item["ItemID"] + "\"\n")
                pass

            """
            Create Bids and Users tables
            """
            if item["Bids"] != None:
                location = "NULL"
                country = "NULL"
                # Check if a bid's location and country is empty, if not then fill vars with values
                for bid in item["Bids"]:
                    if (bid["Bid"]["Bidder"].get("Location") != None):
                        location = bid["Bid"]["Bidder"].get("Location")

                    if (bid["Bid"]["Bidder"].get("Location") != None):
                        country = bid["Bid"]["Bidder"].get("Location")
                    # Write data to respective files
                    bidsDataFile.write("\"" + sub("\"","\"\"",bid["Bid"]["Bidder"]["UserID"]) + "\"|\"" + sub("\"","\"\"",item["ItemID"]) + "\"|\"" + sub("\"","\"\"",transformDollar(bid["Bid"]["Amount"])) + "\"|\"" + sub("\"","\"\"",transformDttm(bid["Bid"]["Time"])) + "\"\n")
                    userDataFile.write("\"" + sub("\"","\"\"",bid["Bid"]["Bidder"]["UserID"]) + "\"|" + bid["Bid"]["Bidder"]["Rating"] + "|\"" + sub("\"","\"\"",location) + "\"|\"" + sub("\"","\"\"",country) + "\"\n")
                    pass
            """
            Finish Users table
            """
            # Write data to Users table file
            userDataFile.write("\"" + sub("\"","\"\"",item["Seller"]["UserID"]) + "\"|" + item["Seller"]["Rating"] + "|\"" + sub("\"","\"\"",item["Location"]) + "\"|\"" + sub("\"","\"\"",item["Country"]) + "\"\n")
"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print "Success parsing " + f

if __name__ == '__main__':
    main(sys.argv)
