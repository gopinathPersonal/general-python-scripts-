SELECT 
	f.title
FROM 
	film f, rental r, inventory i
WHERE 
	f.film_id = i.film_id
	AND i.inventory_id = r.inventory_id
Group By
;