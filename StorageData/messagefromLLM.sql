CREATE TABLE nearyou.messageTableKafka
(
    user_uuid UUID,
    activity_uuid UUID,
    message_uuid UUID,
    message String,
    activityLatitude Float64,
    activityLongitude Float64,
    creationTime String,
    userLatitude Float64,
    userLongitude Float64
) ENGINE = Kafka()
SETTINGS 
    kafka_broker_list = 'kafka:9092',
    kafka_topic_list = 'MessageElaborated',
    kafka_group_name = 'clickhouseConsumerMessage',
    kafka_format = 'JSONEachRow';
--ENGINE = Kafka('kafka:9092', 'MessageElaborated', 'clickhouseConsumerMessage', 'JSONEachRow')
      --SETTINGS kafka_thread_per_consumer = 0, kafka_num_consumers = 1;


CREATE TABLE nearyou.messageTable
(
    user_uuid UUID,
    activity_uuid UUID,
    message_uuid UUID,
    message String,
    activityLatitude Float64,
    activityLongitude Float64,
    creationTime String,
    userLatitude Float64,
    userLongitude Float64
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(toDateTime(creationTime))   -- Partizione per mese basato sul timestamp di creazione
PRIMARY KEY (message_uuid, toStartOfMinute(toDateTime(creationTime)), creationTime)
TTL toDateTime(creationTime) + INTERVAL 1 MONTH   -- I dati saranno conservati per 1 mese
SETTINGS index_granularity = 8192;




CREATE MATERIALIZED VIEW nearyou.mv_messageTable TO nearyou.messageTable
AS
SELECT
    user_uuid,
    activity_uuid,
    message_uuid,
    message,
    activityLatitude,
    activityLongitude,
    creationTime,
    userLatitude,
    userLongitude
FROM nearyou.messageTableKafka;
