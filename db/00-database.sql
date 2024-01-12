-- Database: buyrite

-- DROP DATABASE buyrite;

-- linux
CREATE DATABASE buyrite
	WITH
	OWNER = buyrite_tracker
	ENCODING = 'UTF8'
	TABLESPACE = pg_default
	LC_COLLATE = 'en_US.UTF-8'
	LC_CTYPE = 'en_US.UTF-8'
	CONNECTION LIMIT = -1;

-- windows
CREATE DATABASE buyrite
	WITH
	OWNER = buyrite_tracker
	ENCODING = 'UTF8'
	TABLESPACE = pg_default
	LC_COLLATE = 'English_United States.1252'
	LC_CTYPE = 'English_United States.1252'
	CONNECTION LIMIT = -1;
