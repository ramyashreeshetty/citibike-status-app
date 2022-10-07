# citibike-status-app

Streamlit based web application which uses python and snowflake to display the status of the citibike station in the NY region.
<body>
 &nbsp;
 
  <div>
    <img src="https://user-images.githubusercontent.com/43513353/193456323-32986aec-d341-485b-9648-dbd4c6749b38.png" width="400px" height="250px">
     &nbsp;
    <img src="https://www.nycstreetdesign.info/sites/default/files/2020-01/5.2.3.01%20DOT%20130611%20Citi%20Bike%20Stations%20in%20NYC%20021.jpg" width="400px" height="250px">
  </div>
 &nbsp;
 
  <div>
    The dataset which was used in here: https://gbfs.citibikenyc.com/gbfs/en/station_status.json
  </div>
  &nbsp;
</body>

# How to contribute

- Don't forget to :star: the repository!
- We will be editing the code in GitHub itself so need to clone it locally all you have to do is:

1) Fork this repository.
2) Store this secrets on clipboard or any file.
```
[snowflake]
user = "snowflakedemo"
password = "Snowflake@123"
account = "zx88924.ca-central-1.aws" 
warehouse = "compute_wh"
database = "citibike" 
schema = "public"
```
3) You can do run Streamlit app on your local machine or Streamlit Cloud
    * Local machine
      - Install dependencies and streamlit framework
         ```bash
          pip install streamlit
          pip install -r requirements.txt
        ```
      - Create new file under `.streamlit/secrets.toml` and paste the given text from step 2 
      - Run streamlit app
         ```bash
          streamlit run streamlit_app.py
        ```
    * Streamlit Cloud 
      - Go to [streamlit.io](https://streamlit.io/) and sign-in if you have an account or create a new one (Always choose github sign in)
      - Create a new app on streamlit and select the forked repository and let the main file path remain the as the same!
      - Now click on `Advanced settings` and paste the given text from step 2 into `secrets`.
      - Press `Deploy` and wait for streamlit project provision

4) After deploying you can make changes in ```streamlit.py``` file in github itself by editting and commiting.
5) Create a PR when done. 
:smile: Happy contributing!!!
