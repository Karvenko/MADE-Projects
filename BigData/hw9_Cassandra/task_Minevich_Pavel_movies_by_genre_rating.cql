select min(rating), avg(rating), max(rating) 
from movies_by_genre_rating where genre = 'Sci-Fi' and year >= 2000;
