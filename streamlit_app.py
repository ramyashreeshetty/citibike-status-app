import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('Citibike station')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select * from station_status")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


