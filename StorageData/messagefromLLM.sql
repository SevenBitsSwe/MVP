CREATE TABLE nearyou.messageTableKafka
(
    userID UUID,
    attivitaID UUID,
    id UUID,
    message String,
    activityLatitude Float64,  -- Latitudine dell'attività
    activityLongitude Float64, -- Longitudine dell'attività
    creationTime String,
    userLatitude Float64,  -- Latitudine dell'utente
    userLongitude Float64  -- Longitudine dell'utente
) 
ENGINE = Kafka('kafka:9092', 'MessageElaborated', 'clickhouseConsumerMessage', 'JSONEachRow')
      SETTINGS kafka_thread_per_consumer = 0, kafka_num_consumers = 1;


CREATE TABLE nearyou.messageTable
(
    userID UUID,
    attivitaID UUID,
    id UUID,
    message String,
    activityLatitude Float64,
    activityLongitude Float64,
    creationTime String,
    userLatitude Float64,
    userLongitude Float64
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(toDateTime(creationTime))   -- Partizione per mese basato sul timestamp di creazione
PRIMARY KEY (id, toStartOfMinute(toDateTime(creationTime)), creationTime)
TTL toDateTime(creationTime) + INTERVAL 1 MONTH   -- I dati saranno conservati per 1 mese
SETTINGS index_granularity = 8192;




CREATE MATERIALIZED VIEW nearyou.mv_messageTable TO nearyou.messageTable
AS
SELECT
    userID,
    attivitaID,
    id,
    message,
    activityLatitude,
    activityLongitude,
    creationTime,
    userLatitude,
    userLongitude
FROM nearyou.messageTableKafka;

-- SELECT 
--     m.longitude, 
--     m.latitude, 
--     m.message
-- FROM 
--     (SELECT * 
--      FROM "nearyou"."messageTable" 
--      ORDER BY creationTime DESC 
--      LIMIT 1) AS m
-- INNER JOIN 
--     (SELECT * 
--      FROM "nearyou"."positions" 
--      ORDER BY received_at DESC 
--      LIMIT 1) AS p
-- ON m.id = p.id
-- WHERE geoDistance(p.latitude, p.longitude, m.latitude, m.longitude) <= 400;


          --"rawSql": "SELECT \n    m.longitude, \n    m.latitude, \n    m.message\nFROM \n    (SELECT * \n     FROM \"nearyou\".\"messageTable\" \n     ORDER BY creationTime DESC \n     LIMIT 1) AS m\nINNER JOIN \n    (SELECT * \n     FROM \"nearyou\".\"positions\" \n     ORDER BY received_at DESC \n     LIMIT 1) AS p\nON m.id = p.id\nWHERE geoDistance(p.latitude, p.longitude, m.latitude, m.longitude) <= 400;",
