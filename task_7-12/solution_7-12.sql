/* 7. В подключенном MySQL репозитории создать базу данных “Друзья
человека” */

DROP DATABASE IF EXISTS human_friends;
CREATE DATABASE human_friends;
USE human_friends;

/* 8. Создать таблицы с иерархией из диаграммы в БД */

-- animals

DROP TABLE IF EXISTS animals;
CREATE TABLE animals (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	type_of_animals VARCHAR(45)
);

-- home_animals

DROP TABLE IF EXISTS home_animals;
CREATE TABLE home_animals (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	type_of_animals VARCHAR(45)
);

-- pack_animals

DROP TABLE IF EXISTS pack_animals;
CREATE TABLE pack_animals (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	type_of_animals VARCHAR(45)
);

-- cats

DROP TABLE IF EXISTS cats;
CREATE TABLE cats (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(45),
    birthday DATE,
    commands VARCHAR(50)
);

-- dogs

DROP TABLE IF EXISTS dogs;
CREATE TABLE dogs (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(45),
    birthday DATE,
    commands VARCHAR(50)
);

-- hamsters

DROP TABLE IF EXISTS hamsters;
CREATE TABLE hamsters (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(45),
    birthday DATE,
    commands VARCHAR(50)
);

-- horses

DROP TABLE IF EXISTS horses;
CREATE TABLE horses (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(45),
    birthday DATE,
    commands VARCHAR(50)
);

-- camels

DROP TABLE IF EXISTS camels;
CREATE TABLE camels (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(45),
    birthday DATE,
    commands VARCHAR(50)
);

-- donkeys

DROP TABLE IF EXISTS donkeys;
CREATE TABLE donkeys (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(45),
    birthday DATE,
    commands VARCHAR(50)
);

/* 9. Заполнить низкоуровневые таблицы именами(животных), командами
которые они выполняют и датами рождения */

INSERT INTO cats (name, birthday, commands)
VALUES
('Барсик', '2022-06-13', 'лежать, голос'),
('Васька', '2020-11-04', 'кувырок'),
('Рыжик', '2013-08-16', 'принеси, голос');

INSERT INTO dogs (name, birthday, commands)
VALUES
('Белый клык', '2022-06-24', 'охранять, голос, нельзя'),
('Того', '2020-07-08', 'сидеть, лежать, жди'),
('Балто', '2021-02-05', 'аппорт, лежать, жди');

INSERT INTO hamsters (name, birthday, commands)
VALUES
('Спринтер', '2022-10-07', 'бежать'),
('Пузик', '2020-12-14', 'перевернуться');

INSERT INTO horses (name, birthday, commands)
VALUES
('Бурушка', '2020-04-11', 'рысь, галоп, стоять'),
('Росинант', '2021-08-26', 'вперед, стоять, тише');

INSERT INTO camels (name, birthday, commands)
VALUES
('Вася', '2023-07-02', 'стоять, вперед'),
('Тоффи', '2020-05-11', 'лежать, вперед');

INSERT INTO donkeys (name, birthday, commands)
VALUES
('Осёл', '2023-02-07', 'стоять, вперед'),
('Иван', '2019-03-17', 'стоять, лежать, назад');

/* 10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу. */

DROP TABLE camels;
SELECT h.name AS name, 
	h.birthday AS birthday, 
    h.commands AS commands
FROM horses h
UNION
SELECT d.name, d.birthday, d.commands FROM donkeys d;

/* 11.Создать новую таблицу “молодые животные” в которую попадут все
животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
до месяца подсчитать возраст животных в новой таблице */

DROP TABLE IF EXISTS alltogether;
CREATE TEMPORARY TABLE alltogether AS
SELECT c.name, c.birthday, c.commands FROM cats c
UNION SELECT d.name, d.birthday, d.commands FROM dogs d
UNION SELECT h.name, h.birthday, h.commands FROM hamsters h
UNION SELECT hr.name, hr.birthday, hr.commands FROM horses hr
UNION SELECT dk.name, dk.birthday, dk.commands FROM donkeys dk;

DROP TABLE IF EXISTS young_animals;
CREATE TABLE young_animals AS
SELECT name, birthday, commands,
TIMESTAMPDIFF(month, birthday, now()) AS age_in_month
FROM alltogether
WHERE TIMESTAMPDIFF(year, birthday, now()) BETWEEN 1 AND 3;

/* 12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
прошлую принадлежность к старым таблицам. */

-- FULL JOIN 
SELECT c.*, d.*, h.*, hr.*, dk.* FROM cats c
LEFT JOIN dogs d ON c.id = d.id
LEFT JOIN hamsters h ON d.id = h.id
LEFT JOIN horses hr ON h.id=hr.id
LEFT JOIN donkeys dk ON hr.id=dk.id
UNION
SELECT c.*, d.*, h.*, hr.*, dk.* FROM donkeys dk
LEFT JOIN horses hr ON dk.id = hr.id
LEFT JOIN hamsters h ON hr.id = h.id
LEFT JOIN dogs d ON h.id=d.id
LEFT JOIN cats c ON d.id=c.id;
