CREATE TABLE IF NOT EXISTS movies (
	movieid int PRIMARY KEY,
	title text,
	year int,
	genres set<text>
);
