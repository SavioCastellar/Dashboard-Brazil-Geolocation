from __future__ import barry_as_FLUFL
import encodings
import pandas as pd
from pyproj import get_proj_operations_map
import psycopg2

##### Lista com valores fixos #####
# Criada a partir dos comandos abaixo:

conn = psycopg2.connect(dbname='SGM',
                        user='postgres', 
                        host='ec2-3-95-135-96.compute-1.amazonaws.com',
                        password='trlab2021',                        
                        )
conn.set_client_encoding('UNICODE')

cur = conn.cursor()

cur.execute("""
            SELECT a.state, geoapi_id,
            COUNT(geolocation_id)
            FROM "Request" AS A
            INNER JOIN "Response" AS B
            ON A.request_id = B.request_id
            GROUP BY a.state, geoapi_id;
        """)
bar_graph_df = cur.fetchall()

bar_graph_df = pd.DataFrame(bar_graph_df, columns=["state", "geoapi_id","quantities"])