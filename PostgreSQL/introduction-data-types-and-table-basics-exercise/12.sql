CREATE TABLE minions_birthdays(
	id SERIAL UNIQUE NOT NULL,
	name VARCHAR(50),
	date_of_birth DATE,
	age INTEGER DEFAULT 0,
	present VARCHAR(100),
	party TIMESTAMPTZ
);