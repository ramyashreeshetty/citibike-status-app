import streamlit
import snowflake.connector
import pandas


streamlit.title('Citibike station')

# Initialize connection.
# Uses st.experimental_singleton to only run once.
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from station_status;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

