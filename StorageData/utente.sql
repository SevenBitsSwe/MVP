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
('2de79262-5f93-4d87-a50a-1da1fd433f17', NULL, 'Mario', 'Rossi', 'mario.rossi@example.com', 'M', '1985-05-15', 'Single'),
('3b2342d6-2bf8-44d6-8806-dce8f552e7ca', NULL, 'Laura', 'Bianchi', 'laura.b@example.com', 'F', '1990-03-22', 'Married'),
('dab3d5dd-9820-4ac7-8ef2-87e128868515', NULL, 'Giuseppe', 'Verdi', 'g.verdi@example.com', 'M', '1975-11-30', 'Married'),
('f87fd5ae-cd6d-4126-9ea0-ad6cb774373e', NULL, 'Anna', 'Ferrari', 'a.ferrari@example.com', 'F', '1988-07-18', 'Single'),
('064924ee-4e96-4a2f-933a-f7eeea5a9f63', NULL, 'Marco', 'Romano', 'm.romano@example.com', 'M', '1982-09-25', 'Divorced'),
('1aebe785-74a4-4370-ba61-dc38895ec38e', NULL, 'Sofia', 'Marino', 's.marino@example.com', 'F', '1995-12-03', 'Single'),
('de42ce35-c5fe-4ece-986d-1049994a77b9', NULL, 'Luca', 'Costa', 'l.costa@example.com', 'M', '1980-04-10', 'Married'),
('7b6a6a33-1dfc-4f0f-a260-6d165955507f', NULL, 'Elena', 'Ricci', 'e.ricci@example.com', 'F', '1992-08-28', 'Single'),
('0db554b3-d2a0-4df1-a15f-a0ee802aba80', NULL, 'Paolo', 'Conti', 'p.conti@example.com', 'M', '1987-01-15', 'Married'),
('2bee8a0d-681e-4603-804f-059e6e9115f3', NULL, 'Chiara', 'Mancini', 'c.mancini@example.com', 'F', '1993-06-20', 'Single');
