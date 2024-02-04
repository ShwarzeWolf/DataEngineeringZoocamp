import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

task_3_query = '''
SELECT 
    COUNT(*) 
FROM green_taxi_data gt 
WHERE 
    gt.lpep_pickup_datetime::date = date '2019-09-18' 
    AND gt.lpep_dropoff_datetime::date = date '2019-09-18'
'''

task_4_query = '''
SELECT 
    gt."lpep_pickup_datetime"::date
FROM green_taxi_data gt 
ORDER BY gt.trip_distance DESC 
LIMIT 1
'''

task_5_query = '''
SELECT 
    gtz."Borough", 
    sum(gt."total_amount") as total_amount
FROM green_taxi_data gt 
JOIN green_taxi_zones_data gtz on gtz."LocationID" = gt."PULocationID" 
WHERE gt.lpep_pickup_datetime::date = date '2019-09-18' 
GROUP BY gtz."Borough" order by total_amount
 '''

task_6_query = '''
SELECT 
    gtzdo."Zone"
FROM green_taxi_zones_data gtzpu
JOIN green_taxi_data gt on gt."PULocationID" = gtzpu."LocationID"
JOIN green_taxi_zones_data gtzdo on gt."DOLocationID" = gtzdo."LocationID"
WHERE gtzpu."Zone" = 'Astoria'
AND EXTRACT(YEAR FROM gt."lpep_pickup_datetime") = '2019'
AND EXTRACT(MONTH FROM gt."lpep_pickup_datetime") = '9'
ORDER BY gt."tip_amount" DESC 
LIMIT 1
'''

for task_query in (task_3_query, task_4_query, task_5_query, task_6_query):
    res = pd.read_sql(task_query, con=engine)
    print(res)
    print('---------------------')
