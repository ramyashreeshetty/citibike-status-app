import pandas as pd
from snowflake import connector
import streamlit as st


def get_snowflake_connector():
    # connect to snowflake
    return connector.connect(**st.secrets["snowflake"])


if __name__ == "__main__":
    # Header
    st.markdown("<h2 style='text-align: center; color: #1F3442; font-size:60px;'>Citibike Station 🚲 </h2>", unsafe_allow_html=True)

    # CSS Style
    st.markdown(
        """
    <style>
   
   [class="css-uc1cuc e8zbici2"]{
   background-color: #e9e9fa;
    opacity: 0.3;
    background: linear-gradient(135deg, #c957c855 25%, transparent 25%) -13px 0/ 26px 26px, linear-gradient(225deg, #c957c8 25%, transparent 25%) -13px 0/ 26px 26px, linear-gradient(315deg, #c957c855 25%, transparent 25%) 0px 0/ 26px 26px, linear-gradient(45deg, #c957c8 25%, #e9e9fa 25%) 0px 0/ 26px 26px;
    }
    [class="css-1g1an1w edgvbvh9"]{
    background-color: #EEEEEE;
    border: 2px solid #DCDCDC;
    border-radius: 48px;
    }
    
    [class="css-10trblm e16nr0p30"]{
    opactiy: 0.7;
    background-image: url("https://i.pinimg.com/originals/57/d7/cb/57d7cba19b18b0206767b537bb1245fa.png");
    height:200px;
    width:10%;
    }
    
    [class="css-wgrr2o effi0qh3"]{
     font-size: 120%;
      opactiy: 1;
    }
    [class="css-wgrr2o effi0qh3"]{
     font-size: 120%;
      opactiy: 1;
    }
     [class="main css-k1vhr4 egzxvld3"] {
        background-color: #e5e5f7;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    
#Feature 1: station status and info----------------------------------------------------------------------------->
    # Get snowflake connector
    connector = get_snowflake_connector()

    all_station_info_df = pd.read_sql_query('SELECT * FROM station_info WHERE "STATION_ID" in (SELECT "id" FROM citibike_status);', connector)

    selected_station_name = st.sidebar.selectbox("Choose the station to view the status:", all_station_info_df["STATION_NAME"])
    selected_station_description = all_station_info_df[all_station_info_df["STATION_NAME"] == selected_station_name].reset_index()

    options = int(selected_station_description["STATION_ID"][0])

    all_station_info_df = pd.read_sql_query(f'SELECT * FROM citibike_status WHERE "id" = {options};', connector)
    left_col, right_col = st.columns(2)
    for col_name in all_station_info_df.columns:
        with left_col:
            st.write(*[x.upper() for x in col_name.split("_")], ":")
        with right_col:
            st.write(all_station_info_df[col_name][0])
    
    #Map implementation--->
    mapdata = pd.read_sql_query(f'SELECT * FROM station_info WHERE "station_id" = {options};', connector)
    mapdata = mapdata.rename(columns={"LATITUDE":"lat","LONGITUDE":"lon"})
    st.map(mapdata)
                      
