CREATE DATABASE IF NOT EXISTS course_app;

USE course_app;

CREATE TABLE users (

    username VARCHAR(255)
    UNIQUE NOT NULL,

    password VARCHAR(255)
    NOT NULL,

    created_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP
);