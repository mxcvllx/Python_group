CREATE TABLE boards
(
    id        SERIAL PRIMARY KEY,
    name      varchar(255)       not null,
    trello_id varchar(64) UNIQUE NOT NULL
);

CREATE TABLE lists
(
    id        SERIAL PRIMARY KEY,
    name      varchar(255)       not null,
    trello_id varchar(64) UNIQUE NOT NULL,
    board_id  int REFERENCES boards (id)
);

CREATE TABLE cards
(
    id          SERIAL PRIMARY KEY,
    name        varchar            NOT NULL,
    trello_id   varchar(64) UNIQUE NOT NULL,
    url         varchar(255),
    description text,
    list_id     int REFERENCES lists (id)
);

CREATE TABLE users
(
    id              serial PRIMARY KEY,
    chat_id         bigint UNIQUE NOT NULL,
    first_name       varchar(255),
    last_name       varchar(255),
    username        varchar(255),
    trello_username varchar(255) UNIQUE,
    trello_id       varchar(64) UNIQUE
);


drop table users;

CREATE TABLE boards_users
(
    id       serial,
    board_id int REFERENCES boards (id),
    user_id  int REFERENCES users (id),
    primary key (board_id, user_id)
);

CREATE TABLE cards_users
(
    id      serial,
    card_id int references cards (id),
    user_id int references users (id),
    primary key (card_id, user_id)
);

CREATE TABLE labels
(
    id        SERIAL primary key,
    name      varchar(255)       NOT NULL,
    color     varchar(100),
    trello_id varchar(64) UNIQUE NOT NULL,
    board_id  int references boards (id)
);

CREATE TABLE cards_labels
(
    id       serial,
    card_id  int references cards (id),
    label_id int references labels (id),
    primary key (card_id, label_id)
);

