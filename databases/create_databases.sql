drop database if exists capstone_starter_test;
drop database if exists capstone_starter_development;
drop user capstone_starter;
drop user capstone_starter_test;

create database capstone_starter_development;
create database capstone_starter_test;
create user capstone_starter with password 'capstone_starter';
grant all privileges on database capstone_starter_development to capstone_starter;
grant all privileges on database capstone_starter_test to capstone_starter;

\connect capstone_starter_development
grant usage, create on schema public to capstone_starter;

\connect capstone_starter_test
grant usage, create on schema public to capstone_starter;
