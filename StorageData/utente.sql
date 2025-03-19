CREATE TABLE IF NOT EXISTS nearyou.user(
       user_uuid UUID,
       assigned_sensor_uuid UUID NULL,
       name String,
       surname String,
       email String,
       gender String,
       birthdate Date DEFAULT toDate(now()),
       civil_status String,
       PRIMARY KEY(user_uuid)
) ENGINE = MergeTree()
ORDER BY user_uuid;


INSERT INTO nearyou.user (user_uuid, assigned_sensor_uuid, name, surname, email, gender, birthdate, civil_status) VALUES
('a64d2c83-4e4e-4548-9214-515e11c0453e', NULL, 'Mario', 'Rossi', 'mario.rossi@example.com', 'M', '1985-05-15', 'Single'),
('48872095-944a-4a14-8832-d4d9c9996960', NULL, 'Laura', 'Bianchi', 'laura.b@example.com', 'F', '1990-03-22', 'Married'),
('af6e3f66-7732-4363-9957-9d418070f3ea', NULL, 'Giuseppe', 'Verdi', 'g.verdi@example.com', 'M', '1975-11-30', 'Married'),
('b44c9031-9f70-4094-b19d-c4d7dc69801a', NULL, 'Anna', 'Ferrari', 'a.ferrari@example.com', 'F', '1988-07-18', 'Single'),
('2a39b15a-285a-40bb-912c-98181e781eab', NULL, 'Marco', 'Romano', 'm.romano@example.com', 'M', '1982-09-25', 'Divorced'),
('9c7cfb9e-95a8-4dcb-82c8-2c22384f614e', NULL, 'Sofia', 'Marino', 's.marino@example.com', 'F', '1995-12-03', 'Single'),
('815a28d4-c66d-4b71-a84c-c6fdffdd17ca', NULL, 'Luca', 'Costa', 'l.costa@example.com', 'M', '1980-04-10', 'Married'),
('b21fe281-421c-4edf-955a-910d4aaff7d4', NULL, 'Elena', 'Ricci', 'e.ricci@example.com', 'F', '1992-08-28', 'Single'),
('aac055b2-b691-460b-9b93-68a9c9c70ed7', NULL, 'Paolo', 'Conti', 'p.conti@example.com', 'M', '1987-01-15', 'Married'),
('714e07c1-5b72-43a1-994e-d60e0d1eda6d', NULL, 'Chiara', 'Mancini', 'c.mancini@example.com', 'F', '1993-06-20', 'Single');
