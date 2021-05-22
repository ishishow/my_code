CREATE TABLE
IF NOT EXISTS recipe
(
    "id" VARCHAR
(128) NOT NULL,
    "name" VARCHAR
(64) NOT NULL,
    PRIMARY KEY
("id")
);

CREATE TABLE
IF NOT EXISTS hash_tag
(
    "id" VARCHAR
(128) NOT NULL,
    "name" VARCHAR
(64) NOT NULL,
   `coin` INT UNSIGNED NOT NULL COMMENT '所持コイン',
    PRIMARY KEY
("id")
);

CREATE TABLE
IF NOT EXISTS recipe_hash_tag
(
    "recipe_id" VARCHAR
(128) NOT NULL,
    "hash_tag_id" VARCHAR
(128) NOT NULL,
    UNIQUE
("recipe_id", "hash_tag_id")
);
