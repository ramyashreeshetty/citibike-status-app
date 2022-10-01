import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError

streamlit.title('Citibike station')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# my_cur.execute("select * from station_status")
# my_catalog = my_cur.fetchall()

def load_table_as_dataframe(table):
    # This is super klugy. 
    data = run_query("SELECT * FROM public.{};".format(str(table)))
    columns = run_query("SELECT *FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{}';".format(str(table)))
    # Fish out the actual column names
    columns = [c[3] for c in columns]
    df = pd. DataFrame(data, columns = columns)
    return df

def run_query(query):
  with my_cnx.cursor() as my_cur:
    my_cur.execute(query)
    return my_cur.fetchall()

df = load_table_as_dataframe("station_status") 
streamlit.write(df.columns)


# df = pd.DataFrame(my_catalog)
# df.columns = map(lambda x: str(x).upper(), df.columns)
# streamlit.write(df.columns)
#id_list = df[0].values.tolist()
#df.columns = df.columns.str.upper()
# #streamlit.write(id_list)

# option = streamlit.selectbox('Choose the station id to view the status:', list(id_list))
# if streamlit.button('show status'):
#           my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#           my_cur = my_cnx.cursor()
#           my_cur.execute("select * from station_status id = 72")
#           df2 = my_cur.fetchone()
#           streamlit.write(df2)
          
