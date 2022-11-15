drop database if exists Organic_chem;
create database Organic_chem;
use Organic_chem;
create table Reactions (
    Name varchar(30) NOT NULL,
    Reactant varchar(50),
    Reagent varchar(100) PRIMARY KEY,
    Conditions varchar(20),
    Product varchar(50),
    Remarks text
);