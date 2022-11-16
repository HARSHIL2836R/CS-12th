drop database if exists Organic_chem;
create database Organic_chem;
use Organic_chem;
/* TEXT is a datatype with a field with maximum length of 65535 characters.
Sorts and comparisons on stored data are not case sensitive in TEXT fields.
We do not need to specify a length with TEXT.
TINYTEXT is Text datatype.
It is a TEXT column with a maxiumum length of 255 characters.
We do not need to specify a length with TINYTEXT*/
create table Reactions (
    Name TINYTEXT NOT NULL,
    Reactant TINYTEXT,
    Reagent TINYTEXT NOT NULL,
    Conditions TINYTEXT,
    Product TINYTEXT,
    Remarks TEXT
);