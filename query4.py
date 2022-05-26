from select import select
import pandas as pd
import psycopg2
from pyproj import get_proj_operations_map

conn = psycopg2.connect(dbname='SGM',
                        user='postgres', 
                        host='ec2-3-95-135-96.compute-1.amazonaws.com',
                        password='trlab2021')

cur = conn.cursor()

sql = ("""SELECT date, geolocation_id
            FROM "Search" AS S
            INNER JOIN "Response" AS R
            ON S.request_id = R.request_id
            WHERE date > now() - interval '7 days'
            LIMIT 10;
            """)

cur.execute(sql)
data_frame4 = cur.fetchall()
for i in range(len(data_frame4)):
    print(data_frame4[i][0], data_frame4[1])