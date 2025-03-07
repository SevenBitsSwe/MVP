CREATE TABLE IF NOT EXISTS nearyou.sensor
(
    sensor_uuid UUID PRIMARY KEY,
    is_occupied Boolean DEFAULT false
) ENGINE = MergeTree()
ORDER BY sensor_uuid;


INSERT INTO nearyou.sensor (sensor_uuid, is_occupied)
VALUES 
    (generateUUIDv4(), false),
    (generateUUIDv4(), false),
    (generateUUIDv4(), false),
    (generateUUIDv4(), false),
    (generateUUIDv4(), false),
    (generateUUIDv4(), false),
    (generateUUIDv4(), false),
    (generateUUIDv4(), false),
    (generateUUIDv4(), false),
    (generateUUIDv4(), false);