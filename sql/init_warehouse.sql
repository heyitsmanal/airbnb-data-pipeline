CREATE SCHEMA IF NOT EXISTS airbnb;

CREATE TABLE IF NOT EXISTS airbnb.listings (
    listing_id        BIGINT,
    name              TEXT,
    host_id           BIGINT,
    neighbourhood     TEXT,
    room_type         TEXT,
    price             NUMERIC,
    minimum_nights    INT,
    number_of_reviews INT,
    last_review       DATE,
    reviews_per_month NUMERIC,
    calculated_host_listings_count INT,
    availability_365  INT,
    ingest_ts         TIMESTAMP DEFAULT NOW()
);
