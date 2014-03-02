CREATE TABLE raw_tweets (
	id STRING PRIMARY KEY, -- This may be *very* long, so we store it in a string.
	created STRING,
	text STRING
);
