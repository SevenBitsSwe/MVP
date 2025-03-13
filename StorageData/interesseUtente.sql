CREATE TABLE nearyou.interesseUtente(
       utente UUID,
       interesse String,
       PRIMARY KEY(utente, interesse)
) ENGINE = MergeTree()
ORDER BY (utente, interesse);



INSERT INTO nearyou.interesseUtente (utente, interesse) VALUES
('2bee8a0d-681e-4603-804f-059e6e9115f3', 'Sport'),
('2bee8a0d-681e-4603-804f-059e6e9115f3', 'Natura');