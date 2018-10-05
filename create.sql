drop table if exists Items;
drop table if exists Users;
drop table if exists Categories;
drop table if exists Bids;
create table Items (
  ItemID int,
  UserID varchar(255),
  Name varchar(255),
  Currently varchar(255),
  FirstBid varchar(255),
  NumBids int,
  Location varchar(255),
  Country varchar(255),
  Start varchar(255),
  End varchar(255),
);
create table Users (
  UserID varchar(255),
  Rating int,
  Location varchar(255),
);
create table Categories (
  Category varchar(255),
);
create table Bids (
  UserID varchar(255),
  ItemID int,
  Amount varchar(255),
);
