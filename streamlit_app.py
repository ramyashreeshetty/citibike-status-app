import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('Citibike station')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.fetchall()


