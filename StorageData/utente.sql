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
(generateUUIDv4(), NULL, 'Mario', 'Rossi', 'mario.rossi@example.com', 'M', '1985-05-15', 'Single'),
(generateUUIDv4(), NULL, 'Laura', 'Bianchi', 'laura.b@example.com', 'F', '1990-03-22', 'Married'),
(generateUUIDv4(), NULL, 'Giuseppe', 'Verdi', 'g.verdi@example.com', 'M', '1975-11-30', 'Married'),
(generateUUIDv4(), NULL, 'Anna', 'Ferrari', 'a.ferrari@example.com', 'F', '1988-07-18', 'Single'),
(generateUUIDv4(), NULL, 'Marco', 'Romano', 'm.romano@example.com', 'M', '1982-09-25', 'Divorced'),
(generateUUIDv4(), NULL, 'Sofia', 'Marino', 's.marino@example.com', 'F', '1995-12-03', 'Single'),
(generateUUIDv4(), NULL, 'Luca', 'Costa', 'l.costa@example.com', 'M', '1980-04-10', 'Married'),
(generateUUIDv4(), NULL, 'Elena', 'Ricci', 'e.ricci@example.com', 'F', '1992-08-28', 'Single'),
(generateUUIDv4(), NULL, 'Paolo', 'Conti', 'p.conti@example.com', 'M', '1987-01-15', 'Married'),
(generateUUIDv4(), NULL, 'Chiara', 'Mancini', 'c.mancini@example.com', 'F', '1993-06-20', 'Single');
