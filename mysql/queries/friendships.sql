-- Query: Create 6 new users
INSERT INTO users (first_name, last_name)
VALUES ('Daniel', 'Hernandez'), ('Ethan', 'L'), ('Jim', 'Daddy'), ('Seann', 'Avery'), ('Deborah', 'Na'), ('Terry', 'C');

SELECT * from friendships;
-- Query: Have user 1 be friends with user 2, 4 and 6
INSERT INTO friendships (user_id, friend_id)
VALUES (1,2), (1,4), (1,6); 

-- Query: Have user 2 be friends with user 1, 3 and 5
INSERT INTO friendships (user_id, friend_id)
VALUES (2,1), (2,3), (2,5); 

-- Query: Have user 3 be friends with user 2 and 5
INSERT INTO friendships (user_id, friend_id)
VALUES (3,2), (3,5); 

-- Query: Have user 4 be friends with user 3
INSERT INTO friendships (user_id, friend_id)
VALUES (4,3); 

-- Query: Have user 5 be friends with user 1 and 6
INSERT INTO friendships (user_id, friend_id)
VALUES (5,1), (5, 6); 

-- Query: Have user 6 be friends with user 2 and 3
INSERT INTO friendships (user_id, friend_id)
VALUES (6,2), (6, 3); 

SELECT * from users;

-- Query: Display the relationships create as shown in the above image
SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name
FROM users 
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;


