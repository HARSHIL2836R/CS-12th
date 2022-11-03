drop database if exists organic;
create database organic;
use organic;
create table Reactions (
    Name varchar(30),
    Reactant varchar(50),
    Reagent varchar(100),
    Conditions(Optional) varchar(20),
    Product varchar(50),
    Remarks text
);