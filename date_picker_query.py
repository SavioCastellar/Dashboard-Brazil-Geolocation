from dataclasses import dataclass
from datetime import date as dt, datetime
from select import select
import pandas as pd
import psycopg2
from pyproj import get_proj_operations_map
import geopandas as gpd

conn = psycopg2.connect(dbname='SGM',
                        user='postgres', 
                        host='ec2-3-95-135-96.compute-1.amazonaws.com',
                        password='trlab2021')

cur = conn.cursor()

sql = ("""SELECT date
            FROM "Search"
            ORDER BY 1
            """)
cur.execute(sql)

date_picker_df = cur.fetchall()

date_picker_df = pd.DataFrame(date_picker_df, columns=["date"])
date_picker_df['date'] = date_picker_df['date'].astype(str)
date_picker_df['date'] = date_picker_df['date'].str.slice(0,10)
date_picker_df = date_picker_df.drop_duplicates(keep = 'first', inplace = False)