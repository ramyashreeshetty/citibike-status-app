import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError

streamlit.title('Citibike station')



# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("""select * from citibike_status""")
my_catalog = my_cur.fetchall()
df = pd.DataFrame(my_catalog)

#streamlit.write(df)
hdrs = pd.DataFrame(my_cur.description)

id_list = df[0].values.tolist()
#streamlit.write(id_list)

option = streamlit.selectbox('Choose the station id to view the status:', list(id_list))
if streamlit.button('show status'):
          my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
          my_cur = my_cnx.cursor()
          my_cur.execute("""select * from citibike_status where "id" = """ + option + """; """)
          res = my_cur.fetchall()
          df2=pd.DataFrame(res,columns=hdrs['name']).loc[0]
          for c in hdrs['name']:
                    streamlit.write(c, ":\t", df2.at[c])
          
  
          
