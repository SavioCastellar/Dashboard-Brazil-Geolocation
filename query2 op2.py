### Como padronizar o nome dos estados???

from select import select
import pandas as pd
import psycopg2
from pyproj import get_proj_operations_map

conn = psycopg2.connect(dbname='SGM',
                        user='postgres', 
                        host='ec2-3-95-135-96.compute-1.amazonaws.com',
                        password='trlab2021')

cur = conn.cursor()


cur.execute("""
            SELECT state, geoapi_id,
            COUNT(geolocation_id)
            FROM "Response"
            WHERE state LIKE '%Acre'
            OR state LIKE '%Alagoas'
            OR state LIKE '%_map_'
            OR state LIKE '%_mazonas'
            OR state LIKE '%Bahia'
            OR state LIKE '%Cear_'
            OR state LIKE '%Federal'
            OR state LIKE '%Esp_rito'
            OR state LIKE '%Goi_s'
            OR state LIKE '%Maranh'
            OR state LIKE '%Mato Grosso'
            OR state LIKE '%Mato Grosso _o Sul'
            OR state LIKE '%Minas Gerais'
            OR state LIKE '%Par_'
            OR state LIKE '%Para_ba'
            OR state LIKE '%Pernambuco'
            OR state LIKE '%Piau_'
            OR state LIKE '%Rio _e Janeiro'
            OR state LIKE '%Rio Grande _o Norte'
            OR state LIKE '%Rio Grande _o Sul'
            OR state LIKE '%Rond_nia'
            OR state LIKE '%Roraima'
            OR state LIKE '%Santa Catarina'
            OR state LIKE '%S_o Paulo'
            OR state LIKE '%Sergipe'
            OR state LIKE '%Tocantins'
            GROUP BY state, geoapi_id;
        """)

data_frame2 = cur.fetchall()
data_frame2 = pd.DataFrame(data_frame2, columns=["state", "geoapi_id","quantities"])
# for i in range(len(data_frame2)):
#     print(data_frame2[i])