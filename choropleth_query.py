from os import stat
from select import select
from turtle import st
import pandas as pd
import psycopg2
from pyproj import get_proj_operations_map

conn = psycopg2.connect(dbname='SGM',
                        user='postgres', 
                        host='ec2-3-95-135-96.compute-1.amazonaws.com',
                        password='trlab2021')

cur = conn.cursor()


cur.execute("""SELECT a.state,
            count(geolocation_id)
            FROM "Request" AS A
            INNER JOIN "Response" AS B
            ON A.request_id = B.request_id
            GROUP BY a.state;""")
df = cur.fetchall()
df = pd.DataFrame(df, columns=['state', 'count'])

state_df = pd.DataFrame(df, columns=["state", "count"])