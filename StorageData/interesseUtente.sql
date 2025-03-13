CREATE TABLE nearyou.user_interest(
       user_uuid UUID,
       interest String,
       PRIMARY KEY(user_uuid, interest)
) ENGINE = MergeTree()
ORDER BY (user_uuid, interest);


INSERT INTO nearyou.user_interest (user_uuid, interest) VALUES
('a64d2c83-4e4e-4548-9214-515e11c0453e', 'Sport'), 
('a64d2c83-4e4e-4548-9214-515e11c0453e', 'Natura'),
('48872095-944a-4a14-8832-d4d9c9996960', 'Ristorazione'),
('48872095-944a-4a14-8832-d4d9c9996960', 'Cultura'),
('af6e3f66-7732-4363-9957-9d418070f3ea', 'Musica'),
('af6e3f66-7732-4363-9957-9d418070f3ea', 'Viaggi'),
('b44c9031-9f70-4094-b19d-c4d7dc69801a', 'Tecnologia'),
('b44c9031-9f70-4094-b19d-c4d7dc69801a', 'Cinema'),
('2a39b15a-285a-40bb-912c-98181e781eab', 'Moda'),
('2a39b15a-285a-40bb-912c-98181e781eab', 'Arte'),
('9c7cfb9e-95a8-4dcb-82c8-2c22384f614e', 'Fitness'),
('9c7cfb9e-95a8-4dcb-82c8-2c22384f614e', 'Sport'),
('815a28d4-c66d-4b71-a84c-c6fdffdd17ca', 'Natura'),
('815a28d4-c66d-4b71-a84c-c6fdffdd17ca', 'Fotografia'),
('b21fe281-421c-4edf-955a-910d4aaff7d4', 'Teatro'),
('b21fe281-421c-4edf-955a-910d4aaff7d4', 'Cultura'),
('aac055b2-b691-460b-9b93-68a9c9c70ed7', 'Educazione'),
('aac055b2-b691-460b-9b93-68a9c9c70ed7', 'Musica'),
('714e07c1-5b72-43a1-994e-d60e0d1eda6d', 'Giochi'),
('714e07c1-5b72-43a1-994e-d60e0d1eda6d', 'Cinema');