from select import select
from datetime import date
import pandas as pd
import psycopg2
from pyproj import get_proj_operations_map
import geopandas as gpd

conn = psycopg2.connect(dbname='SGM',
                        user='postgres', 
                        host='ec2-3-95-135-96.compute-1.amazonaws.com',
                        password='trlab2021')

cur = conn.cursor()

sql = ("""SELECT date, latitude, longitude, R.geoapi_id
            FROM "Search" AS S
            INNER JOIN "Response" AS R
            ON S.request_id = R.request_id
            WHERE date > now() - interval '7 days'
            ORDER BY 1
            LIMIT 1000
            """)
cur.execute(sql)


scatter_df = cur.fetchall()


scatter_df = pd.DataFrame(scatter_df, columns=["date", "latitude", "longitude","geoapi_id"])
scatter_df['date'] = scatter_df['date'].astype(str)
scatter_df['date'] = scatter_df['date'].str.slice(0,10)