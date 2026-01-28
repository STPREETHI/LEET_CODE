SELECT id,movie,description,rating from Cinema
Where id%2!=0
AND description !='boring'
ORDER BY rating DESC;