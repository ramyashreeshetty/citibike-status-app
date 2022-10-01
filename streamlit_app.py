import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('Citibike station')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select * from station_status)
my_catalog = my_cur.fetchall()

df = pandas.DataFrame(my_catalog)
streamlit.write(df)



