-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit

--sqlite3 /workspaces/semester2-week2/session_1/2_practice/library.db
--.read /workspaces/semester2-week2/session_1/2_practice/code.sql
-- write your sql code here
--Show book title, member name, and loan date.
--SELECT books.title, members.name, loans.loan_date
--FROM Books JOIN Loans ON Books.id=Loans.books_id
--AND Members Join Loans ON Members.id=Loans.members_ID;
--List all books and any loans associated with them.
SELECT Books.title,Loans.loan_date FROM 
Books LEFT JOIN Loans ON Books.id=Loans.book_id;