CREATE TABLE nearyou.interest(
       interest String,
       PRIMARY KEY(interest)
) ENGINE = MergeTree()
ORDER BY (interest);


INSERT INTO nearyou.interest (interest) VALUES
('Ristorazione'),
('Cultura'),
('Natura'),
('Sport'),
('Tecnologia'),
('Moda'),
('Arte'),
('Musica'),
('Viaggi'),
('Fitness'),
('Educazione'),
('Giochi'),
('Fotografia'),
('Cinema'),
('Teatro');;
