/*
a) The actor table includes: actor_id, first_name, last_name, and last_update.

b) The film table includes: film_id, title, description, release_year, language_id,
   rental_duration, rental_rate, length, replacement_cost, rating, special_features,
   and last_update.

c) The film_actor table contains both actor_id and film_id.
   It links actors to the films they appeared in.

d) The rental table includes: rental_id, rental_date, inventory_id, customer_id,
   return_date, staff_id, and last_update. It is hard to read because it only
   shows ID numbers instead of actual names.

e) The inventory table includes: inventory_id, film_id, store_id, and last_update.
   It tracks how many copies of each film exist and where they are stored.

f) You need the rental, inventory, and film tables. They are connected in a chain:
   rental → inventory → film, using inventory_id and film_id as the linking columns.
   This allows you to trace a rental date all the way to a film title.
*/

SELECT rental_id, rental_id, inventory_id FROM rental;
SELECT inventory_id, film_id from inventory; 
SELECT film_id, title FROM film;