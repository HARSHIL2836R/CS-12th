set path=C:\Program Files\MySQL\MySQL Server 5.7\bin
set /p ver=Enter the version of database to be imported:
mysqldump -u root -p Organic_chem < the_db%ver%.sql --port=2836