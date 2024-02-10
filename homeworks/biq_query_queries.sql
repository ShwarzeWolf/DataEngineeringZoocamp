-- setup part
CREATE OR REPLACE EXTERNAL TABLE `ny_taxi_green.taxi_info`
OPTIONS (
  format = 'parquet',
  uris = ['gs://sch_wolf_green_ny_taxi_data/green-taxi/green_tripdata_2022-*.parquet']
);

CREATE OR REPLACE TABLE `ny_taxi_green.taxi_info_bq`
AS SELECT * FROM `ny_taxi_green.taxi_info`;

-- task 1
SELECT COUNT(*) FROM `ny_taxi_green.taxi_info_bq`;

-- task 2
SELECT COUNT(DISTINCT(PULocationID)) FROM `ny_taxi_green.taxi_info`;
SELECT COUNT(DISTINCT(PULocationID)) FROM `ny_taxi_green.taxi_info_bq`;

-- task 3
SELECT COUNT(*) FROM `ny_taxi_green.taxi_info_bq`
WHERE fare_amount = 0;

-- task 4
CREATE OR REPLACE TABLE `ny_taxi_green.taxi_info_partitioned`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS (
  SELECT * FROM `ny_taxi_green.taxi_info`
);

-- task 5
SELECT DISTINCT(PULocationID) FROM `ny_taxi_green.taxi_info_bq`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

SELECT DISTINCT(PULocationID) FROM `ny_taxi_green.taxi_info_partitioned`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';





