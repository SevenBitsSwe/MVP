CREATE TABLE nearyou.testKafka (
                           user_uuid UUID,
                           latitude Float64,
                           longitude Float64,
                           received_at String
) ENGINE = Kafka()
SETTINGS 
    kafka_broker_list = 'kafka:9092',
    kafka_topic_list = 'TestTopic',
    kafka_group_name = 'clickhouseConsumePositions',
    kafka_format = 'JSONEachRow';



CREATE TABLE nearyou.test_kafka
(
    user_uuid UUID,
    latitude Float64,
    longitude Float64,
    received_at String
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(toDateTime(received_at))  -- Partizioniamo per mese in base al campo received_at
PRIMARY KEY (user_uuid, toStartOfMinute(toDateTime(received_at)), received_at)
TTL toDateTime(received_at) + INTERVAL 1 MONTH  -- I dati vengono conservati per un mese
SETTINGS index_granularity = 8192;


CREATE MATERIALIZED VIEW nearyou.mv_test_kafka TO nearyou.test_kafka
AS
SELECT
    user_uuid,
    latitude,
    longitude,
    received_at
FROM nearyou.testKafka;
