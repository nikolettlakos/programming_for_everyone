CREATE TABLE dictionary
(
  dictionary_id  SERIAL NOT NULL
    CONSTRAINT dictionary_dictionary_id_pk
    PRIMARY KEY,
  hungarian_word VARCHAR(9000),
  english_word   VARCHAR(9000),
  meaning        VARCHAR(9000)
);

CREATE UNIQUE INDEX dictionary_dictionary_id_uindex
  ON dictionary (dictionary_id);

CREATE TABLE topic
(
  topic_id   SERIAL NOT NULL
    CONSTRAINT topic_id_pk
    PRIMARY KEY,
  title      VARCHAR(3000),
  body       VARCHAR(3000),
  topic_type VARCHAR(3000),
  fav        INTEGER DEFAULT 0,
  learnt     INTEGER DEFAULT 0
);

CREATE TABLE comment
(
  comment_id   SERIAL NOT NULL
    CONSTRAINT comment_comment_id_pk
    PRIMARY KEY,
  comment      VARCHAR(3000),
  comment_time TIMESTAMP
);

CREATE UNIQUE INDEX comment_comment_id_uindex
  ON comment (comment_id);

CREATE TABLE users
(
  username   VARCHAR(3000),
  first_name VARCHAR(3000),
  last_name  VARCHAR(3000),
  id         SERIAL NOT NULL
    CONSTRAINT users_id_pk
    PRIMARY KEY
);

CREATE UNIQUE INDEX users_id_uindex
  ON users (id);

