-- DOJOS AND NINJAS QUERIES

-- 1. CREATE 3 NEW DOJOS
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('Chicago Dojo', now(), now());
INSERT INTO dojos (name, created_at, updated_at)
Values('LA Dojo', now(), now());

INSERT INTO dojos (name, created_at, updated_at)
VALUES ('Seattle Dojo', now(), now());
-- 2. Query: Delete the 3 dojos you just created
DELETE from dojos
WHERE id=1;
DELETE from dojos
WHERE id=2;
DELETE from dojos
WHERE id=3;

-- 3. Query: Create 3 more dojos
Insert into dojos(name, created_at, updated_at) Values('Blue Dojo', now(), now());
Insert into dojos(name, created_at, updated_at) Values("Red Dojo", now(), now());
Insert into dojos(name, created_at, updated_at) Values("Red Dojo", now(), now());

-- 4. Query: Create 3 ninjas that belong to the first dojo
Insert into ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
Values('Naruto', 'Uzumaki', 14, now(), now(), 7);

SELECT * from ninjas;

Insert into ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
Values('Sasuke', 'Itachi', 15, now(), now(), 7);

Insert into ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
Values('Sakura', 'Haruno', 14, now(), now(), 7);

-- 5. Query: Create 3 ninjas that belong to the second dojo
Insert into ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
Values('Momochi', 'Sandayu', 32, now(), now(), 8);

Insert into ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
Values('Momo', 'Sand', 27, now(), now(), 8);

Insert into ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
Values('Takoyaki', 'Octopus', 2, now(), now(), 8);

-- 6. Query: Create 3 ninjas that belong to the third dojo
Insert into ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
Values('Banana', 'Foster', 110, now(), now(), 9);

Insert into ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
Values('Peanut', 'Butter', 300, now(), now(), 9);

Insert into ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
Values('Crab', 'Lobster', 7, now(), now(), 9);

SELECT * FROM dojos;

-- 7. Query: Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas
WHERE dojo_id=7;

-- 8. Query: Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas
WHERE dojo_id=9;

-- 9. Query: Retrieve the last ninja's dojo
SELECT * FROM ninjas JOIN dojos on dojos.id=ninjas.id
WHERE ninjas.id=9

