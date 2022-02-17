-- Query: Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu
SELECT* from authors;
INSERT INTO authors (name)
VALUES ('Jane Austen'), ('Emily Dickinson'), ('Fyodor Dostoevsky'), ('William Shakespeare'), ('Lau Tzu');

-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books (title, num_of_pages)
VALUES ('C Sharp', 200);
INSERT INTO books (title, num_of_pages)
VALUES ('Java', 150);
INSERT INTO books (title, num_of_pages)
VALUES ('Python', 160);
INSERT INTO books (title, num_of_pages)
VALUES ('PHP', 140);
INSERT INTO books (title, num_of_pages)
VALUES ('RUBY', 165);

-- Query: Change the name of the C Sharp book to C#
UPDATE books SET title = 'C#' 
WHERE id=1; 

SELECT * from favorites;

-- Query: Change the first name of the 4th author to Bill
UPDATE authors SET name = 'Bill Shakespeare'
WHERE id = 4; 

-- Query: Have the first author favorite the first 2 books
INSERT INTO favorites (author_id, book_id)
VALUES (1,1),(1,2);
-- Query: Have the second author favorite the first 3 books
INSERT INTO favorites (author_id, book_id)
VALUES (2,1),(2,2), (2,3);
-- uery: Have the third author favorite the first 4 books
INSERT INTO favorites (author_id, book_id)
VALUES (3,1),(3,2), (3,3), (3,4);
-- Query: Have the fourth author favorite all the books
INSERT INTO favorites (author_id, book_id)
VALUES (4,1),(4,2), (4,3), (4,4), (4,5);

-- Query: Retrieve all the authors who favorited the 3rd book
SELECT * FROM authors JOIN favorites ON authors.id = favorites.author_id
WHERE book_id=3;

-- Query: Remove the first author of the 3rd book's favorites
DELETE from favorites
WHERE book_id=3 AND author_id=2;

SELECT * from favorites;

-- Query: Add the 5th author as an other who favorited the 2nd book
INSERT INTO favorites (author_id, book_id)
VALUES (5,2);

-- Find all the books that the 3rd author favorited
SELECT * from authors JOIN favorites on authors.id =favorites.author_id
JOIN books ON books.id = favorites.book_id
WHERE authors.id =3;

-- Query: Find all the authors that favorited to the 5th book
SELECT * from books JOIN favorites on books.id =favorites.book_id
JOIN authors ON authors.id = favorites.author_id
WHERE books.id =5;

SELECT * from books; 





