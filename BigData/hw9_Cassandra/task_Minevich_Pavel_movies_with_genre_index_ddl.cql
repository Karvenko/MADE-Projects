CREATE TABLE IF NOT EXISTS movies_with_genre_index (
	movieid int PRIMARY KEY,
	title text,
	year int,
	genres set<text>
);
CREATE INDEX genre_idx ON movies_with_genre_index (genres);
