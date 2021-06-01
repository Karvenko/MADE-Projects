CREATE TABLE IF NOT EXISTS movies_by_genre_rating (
	movieid int,
	userid int,
	title text,
	year int,
	genre text,
	rating float, PRIMARY KEY (genre, year, movieid, userid)
);
