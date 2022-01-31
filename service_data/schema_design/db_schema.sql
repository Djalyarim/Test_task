-- -- Создание отдельной схемы для контента:
CREATE SCHEMA IF NOT EXISTS userweight;

SET search_path TO userweight, public;

-- Создание таблицы 'Информация о пользователях': 
CREATE TABLE IF NOT EXISTS userweight.user_weight (
    id              uuid PRIMARY KEY,
    user_id         INT,
    day             DATE,
    weight          FLOAT
);