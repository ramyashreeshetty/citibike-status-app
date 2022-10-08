import requests

import pandas as pd
from snowflake import connector
import streamlit as st


def get_snowflake_connector():
    # connect to snowflake
    return connector.connect(**st.secrets["snowflake"])


def perform_query(connector, query: str):
    # Perform snowflake query
    cursor = connector.cursor()
    cursor.execute(query)
    catalog = cursor.fetchall()
    description = cursor.description

    return catalog, description


if __name__ == "__main__":
    # Header
    st.markdown("<h1 style='text-align: center; color: black; font-size:60px;'>Citibike Station 🚲 </h1>", unsafe_allow_html=True)

    # CSS Style
    st.markdown(
        """
    <style>
    [class="main css-k1vhr4 egzxvld3"] {
        background-color: lightblue;
        background-color: #a1d1e6;
        opacity: 0.8;
        background: linear-gradient(135deg, #a197ba55 25%, transparent 25%) -27px 0/ 54px 54px, linear-gradient(225deg, #a197ba 25%, transparent 25%) -27px 0/ 54px 54px, linear-gradient(315deg, #a197ba55 25%, transparent 25%) 0px 0/ 54px 54px, linear-gradient(45deg, #a197ba 25%, #a1d1e6 25%) 0px 0/ 54px 54px;
       }
    
    [class="css-1g1an1w edgvbvh9"]{
    background-color: #EEEEEE:
    border: 2px solid #DCDCDC;
    border-radius: 48px;
    }
    
    [class="css-10trblm e16nr0p30"]{
    background-image: url("https://img.freepik.com/free-vector/lake-river-city-buildings-skyline_107791-9055.jpg?size=626&ext=jpg");
    height:200px;
    width:10%;
    }
    
    [class="css-wgrr2o effi0qh3"]{
     font-size: 150%;
    }
    [class="css-wgrr2o effi0qh3"]{
     font-size: 150%;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    
#Feature 1: station status----------------------------------------------------------------------------->
    # Get snowflake connector
    connector = get_snowflake_connector()

    # Get citibike id list
    all_citibike, all_citibike_description = perform_query(connector, "SELECT * FROM citibike_status")
    all_citibike_df = pd.DataFrame(all_citibike)
    all_citibike_description_df = pd.DataFrame(all_citibike_description)
    all_citibike_id_list = all_citibike_df[0].values.tolist()

    options = st.selectbox("Choose the station id to view the status:", list(all_citibike_id_list))
    if st.button("Show Status"):
        # Focus only specific id
        specific_citibike, specific_description = perform_query(
            connector, f'SELECT * FROM citibike_status WHERE "id" = {options};'
        )

        specific_citibike_df = pd.DataFrame(specific_citibike, columns=all_citibike_description_df["name"]).loc[0]
        left_col, right_col = st.columns(2)

        # Re-adjust result
        for col_name in all_citibike_description_df["name"]:
            with left_col:
                st.write(*[x.upper() for x in col_name.split("_")], ":")
            with right_col:
                st.write(specific_citibike_df.at[col_name])
                
                
#Feature 2: station info----------------------------------------------------------------------------->
        #new feature-------------------------------------------------------------------------------->
    
    station_info, station_desc = perform_query(connector,"select * from station_info")
    station_info_df = pd.DataFrame(station_info)
    station_info_id_list = station_info_df[0].values.tolist()

    #option
    options = st.selectbox('Choose the station id to view the station information:', list(station_info_id_list))
    if st.button('Show Info'):
        # Focus only specific id
        specific_station, specific_station_description = perform_query(
        connector, f'SELECT * FROM station_info WHERE "STATION_ID" = {options};'
    )

        st.write('Station name: ', specific_station[0][3])

                  
