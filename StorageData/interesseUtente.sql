CREATE TABLE IF NOT EXISTS nearyou.interesseUtente(
       utente UUID,
       interesse String,
       PRIMARY KEY(utente, interesse)
) ENGINE = MergeTree()
ORDER BY (utente, interesse);

INSERT INTO nearyou.interesseUtente (utente, interesse) VALUES
(toUUID('306ef53f-9222-4e9f-bb47-07ed6c2009ab'), 'Sport'),
(toUUID('306ef53f-9222-4e9f-bb47-07ed6c2009ab'), 'Natura');