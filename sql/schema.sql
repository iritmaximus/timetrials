CREATE TABLE IF NOT EXISTS users (
  id serial primary key,
  name varchar(80) not null,
  password varchar(80) not null
);

CREATE TABLE IF NOT EXISTS games (
  id serial primary key,
  name varchar(80) not null
);

CREATE TABLE IF NOT EXISTS cups (
  id serial primary key,
  name varchar(80) not null
);

CREATE TABLE IF NOT EXISTS courses (
  id serial primary key,
  name varchar(80) not null,
  game_id int references games(id),
  cup_id int references cups(id)
);


CREATE TABLE IF NOT EXISTS standards (
  id serial primary key,
  name varchar(50) not null,
  tier varchar(3),
  points numeric,
  course_id int references courses(id)
);

CREATE TABLE IF NOT EXISTS times (
  id serial primary key,
  game_id int references games(id),
  course_id int references courses(id),
  timems varchar(80),
  date date
);
