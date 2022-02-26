-- MySQL functions

-- Text
-- Concat()
SELECT CONCAT('Mr.',' ', first_name, ' ' , last_name) AS full_name FROM users;
-- CONCAT WS()
SELECT CONCAT_WS(' ', first_name, last_name, 'cool') AS full_name FROM users;
-- LENGTH()
SELECT LENGTH(last_name) AS last_len from users;
-- LOWER()
SELECT LOWER(first_name) AS first_lowercase FROM users;
-- DATE
-- HOUR()
SELECT HOUR(joined_datetime) AS date_hour, joined_datetime FROM users;
-- DAYNAME()
SELECT DAYNAME(joined_datetime)AS date_name, joined_datetime FROM users;
-- MONTH()
SELECT MONTH(joined_datetime)AS month_number, joined_datetime from users;
-- NOW()
SELECT NOW() AS right_now;
-- DATE FORMAT()
SELECT DATE_FORMAT(joined_datetime, '%W, %M, %e, %Y') from users;