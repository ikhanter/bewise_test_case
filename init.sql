CREATE TABLE questions (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    question_id bigint UNIQUE,
    question varchar(255),
    answer varchar(255),
    created_at timestamp with time zone,
    added timestamp
);