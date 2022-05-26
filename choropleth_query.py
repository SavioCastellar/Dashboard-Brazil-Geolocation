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


cur.execute("""SELECT state, count(geolocation_id) FROM "Response" GROUP BY state;""")
df = cur.fetchall()

##### RELATÓRIO DE ERRO #####
# A lista de tuplas gerada pela query contém strings com caracteres que não podem ser decodificados pelo python.
# Exemplo: Ceará pode ser encontrado na tabela como 'Ceara' e 'Cear�'
# return codecs.charmap_encode(input,self.errors,encoding_table)[0]
# UnicodeEncodeError: 'charmap' codec can't encode characters in position 1239-1240: character maps to <undefined>

cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Acre' GROUP BY state;""")
AC = cur.fetchall()
AC = ('AC', AC[0][1])


cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Alagoas' GROUP BY state;""")
AL = cur.fetchall()
AL = ('AL', AL[0][1])


sumAP = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Amap%' GROUP BY state;""")
AP = cur.fetchall()
for i in range(len(AP)):
    sumAP = sumAP + AP[i][1]
AP = ('AP', sumAP)


cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Amazonas' GROUP BY state;""")
AM = cur.fetchall()
AM = ('AM', AM[0][1])


cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Bahia' GROUP BY state;""")
BA = cur.fetchall()
BA = ('BA', BA[0][1])


sumCE = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Cear%' GROUP BY state;""")
CE = cur.fetchall()
for i in range(len(CE)):
    sumCE = sumCE + CE[i][1]
CE = ('CE', sumCE)


sumDF = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Federal%' GROUP BY state;""")
DF = cur.fetchall()
for i in range(len(DF)):
    sumDF = sumDF + DF[i][1]
DF = ('DF', sumDF)


sumES = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Esp%' GROUP BY state;""")
ES = cur.fetchall()
for i in range(len(ES)):
    sumES = sumES + ES[i][1]
ES = ('ES', sumES)


sumGO = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Goi%' GROUP BY state;""")
GO = cur.fetchall()
for i in range(len(GO)):
    sumGO = sumGO + GO[i][1]
GO = ('GO', sumGO)


sumMA = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Maranh%' GROUP BY state;""")
MA = cur.fetchall()
for i in range(len(MA)):
    sumMA = sumMA + MA[i][1]
MA = ('MA', sumMA)


sumMT = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Mato Grosso' GROUP BY state;""")
MT = cur.fetchall()
for i in range(len(MT)):
    sumMT = sumMT + MT[i][1]
MT = ('MT', sumMT)


sumMS = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Mato Grosso _o Sul' GROUP BY state;""")
MS = cur.fetchall()
for i in range(len(MS)):
    sumMS = sumMS + MS[i][1]
MS = ('MS', sumMS)


sumMG = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Minas%' GROUP BY state;""")
MG = cur.fetchall()
for i in range(len(MG)):
    sumMG = sumMG + MG[i][1]
MG = ('MG', sumMG)


sumPA = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Par_' GROUP BY state;""")
PA = cur.fetchall()
for i in range(len(PA)):
    sumPA = sumPA + PA[i][1]
PA = ('PA', sumPA)


sumPR = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Paran_' GROUP BY state;""")
PR = cur.fetchall()
for i in range(len(PR)):
    sumPR = sumPR + PR[i][1]
PR = ('PR', sumPR)


sumPB = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Para_ba' GROUP BY state;""")
PB = cur.fetchall()
for i in range(len(PB)):
    sumPB = sumPB + PB[i][1]
PB = ('PB', sumPB)


sumPE = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Pernambuco' GROUP BY state;""")
PE = cur.fetchall()
for i in range(len(PE)):
    sumPE = sumPE + PE[i][1]
PE = ('PE', sumPE)


sumPI = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Piau_' GROUP BY state;""")
PI = cur.fetchall()
for i in range(len(PI)):
    sumPI = sumPI + PI[i][1]
PI = ('PI', sumPI)


sumRJ = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Rio _e Janeiro' GROUP BY state;""")
RJ = cur.fetchall()
for i in range(len(RJ)):
    sumRJ = sumRJ + RJ[i][1]
RJ = ('RJ', sumRJ)


sumRN = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Rio Grande _o Norte' GROUP BY state;""")
RN = cur.fetchall()
for i in range(len(RN)):
    sumRN = sumRN + RN[i][1]
RN = ('RN', sumRN)

sumRS = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Rio Grande _o Sul' GROUP BY state;""")
RS = cur.fetchall()
for i in range(len(RS)):
    sumRS = sumRS + RS[i][1]
RS = ('RS', sumRS)


sumRO = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Rond_nia' GROUP BY state;""")
RO = cur.fetchall()
for i in range(len(RO)):
    sumRO = sumRO + RO[i][1]
RO = ('RO', sumRO)

cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Roraima' GROUP BY state;""")
RR = cur.fetchall()
RR = ('RR', RR[0][1])


sumSC = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Santa Catarina' GROUP BY state;""")
SC = cur.fetchall()
for i in range(len(SC)):
    sumSC = sumSC + SC[i][1]
SC = ('SC', sumSC)


sumSP = 0
cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%S_o Paulo' GROUP BY state;""")
SP = cur.fetchall()
for i in range(len(SP)):
    sumSP = sumSP + SP[i][1]
SP = ('SP', sumSP)


cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Sergipe' GROUP BY state;""")
SE = cur.fetchall()
SE = ('SE', SE[0][1])

cur.execute("""SELECT state, count(geolocation_id) FROM "Response" WHERE state LIKE '%Tocantins' GROUP BY state;""")
TO = cur.fetchall()
TO = ('TO', TO[0][1])


state_df = [AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PR, PB, PE, PI, RJ, RN, RS, RJ, RO, RR, SC, SP, SE, TO]
state_df = pd.DataFrame(state_df, columns=["state", "count"])


# df = pd.DataFrame(df, columns=["state", "count"])

# df = df.apply(lambda x: x.astype(str).str.lower())

# df['state'] = df['state'].str.replace('state of ', '')
# df['state'] = df['state'].str.replace('federal district', 'distrito federal')
# df['state'] = df['state'].str.replace('í', 'i')
# df['state'] = df['state'].str.replace('á', 'a')
# df['state'] = df['state'].str.replace('ã', 'a')
# df['state'] = df['state'].str.replace('ô', 'o')

# state_initials_map = {
#     'acre': 'ac',
#     'alagoas': 'al',
#     'amapa': 'ap',
#     'amazonas': 'am',
#     'bahia': 'ba',
#     'ceara': 'ce',
#     'distrito federal': 'df',
#     'espirito santo': 'es',
#     'goias': 'go',
#     'maranhao': 'ma',
#     'mato grosso': 'mt',
#     'mato grosso do sul': 'ms',
#     'minas gerais': 'mg',
#     'para': 'pa',
#     'paraiba': 'pb',
#     'parana': 'pr',
#     'pernambuco': 'pe',
#     'piaui': 'pi',
#     'rio de janeiro': 'rj',
#     'rio grande do norte': 'rn',
#     'rio grande do sul': 'rs',
#     'rondonia': 'ro',
#     'roraima': 'rr',
#     'santa catarina': 'sc',
#     'sao paulo': 'sp',
#     'sergipe': 'se',
#     'tocantins': 'to'
# }

# df = df.replace({'state': state_initials_map})

# df['count'] = pd.to_numeric(df['count'])

# aggregation_map = {
#     'state': 'first',
#     'count': 'sum'
# }

# df = df.groupby('state', as_index=False).aggregate(aggregation_map)

# df = df.drop(labels=[3, 12, 15, 24, 30])

# df = df.apply(lambda x: x.astype(str).str.upper())

# state_df = pd.DataFrame(df, columns=['state', 'count'])