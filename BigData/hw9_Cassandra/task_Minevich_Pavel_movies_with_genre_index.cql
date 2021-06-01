select count(*) from movies_with_genre_index
	where genres contains 'Horror' and 
	year >= 1980 and year <= 1990 allow filtering;
