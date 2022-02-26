-- find all the clients (first and last name) billing amount and charge date time
SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
FROM clients
JOIN billing ON clients.id=billing.clients_id;
-- list all the domain names and leads (first and last_name) for each site.
SELECT sites.domain_name, leads.first_name, leads.last_name
FROM sites
JOIN leads on sites.id = leads.sites_id;
-- Join on multiple tables
-- get the names of the clients, their domain names and the first names of all the leads generated from their sites.
SELECT clients.first_name AS client_first, clients. last_name, sites.domain_name, leads.first_name AS leads_first
FROM clients
JOIN sites on clients.id = sites.clients_id
JOIN leads on sites.id = leads.sites_id;
-- LEFT AND RIGHT JOIN
-- LIST all the clients and the sites each client has, even if the client hasnt landed a site yet.
SELECT clients.first_name, clients.last_name, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.id= sites.clients_id;
-- adding billing sum to only have one name and sum of amount
-- Grouping by
-- there's MAX, MIN, AVG
-- always use a function with group by
SELECT clients.first_name, clients.last_name, AVG(billing.amount)
FROM clients
JOIN billing ON clients.id= billing.clients_id
GROUP BY clients.id;
-- group CONCAT() we want the client to be named once and not more
SELECT GROUP_CONCAT( sites.domain_name) AS domains, clients.first_name, clients.last_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP BY clients.id;
-- COUNT
-- find total number of leads for each site.
SELECT COUNT(leads.id), sites.domain_name
from sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;