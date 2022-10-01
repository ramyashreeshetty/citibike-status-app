import streamlit
import snowflake.connector
import pandas


streamlit.title('Citibike station')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select station to know the status")



