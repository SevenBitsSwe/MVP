CREATE TABLE IF NOT EXISTS nearyou.utente(
       id UUID,
       nome String,
       cognome String,
       email String,
       genere String,
       data_nascita Date DEFAULT toDate(now()),
       stato_civile String,
       PRIMARY KEY(id)
) ENGINE = MergeTree()
ORDER BY id;

INSERT INTO nearyou.utente (id, nome, cognome, email, genere, data_nascita, stato_civile) VALUES
(toUUID('306ef53f-9222-4e9f-bb47-07ed6c2009ab'), 'Mario', 'Rossi', 'mario.rossi@example.com', 'M', '1985-05-15', 'Single');
