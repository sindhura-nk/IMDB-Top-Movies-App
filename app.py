import streamlit as st
import pandas as pd
from  utils import api_extracter

#initialise streamlit app
st.set_page_config(page_title="IMDB Movies Project",layout="wide")

# initalise imdb movie client by creating an instance of it
client = api_extracter()

# show the title of the project
st.title("IMDB Movies Web application")
st.subheader("BY Sindhura Nadendla")

# create a button to display popular movies
button = st.button("Display the most latest popular movies")

# After clicking the button, list of movies should get displayed
if button:
    data = client.get_data()
    df = pd.DataFrame(data,columns=["Movie Name","Release Year","Rank"])
    st.dataframe(df)

    csv_data = df.to_csv(index=False).encode("utf-8")
    # DOwnload button for user
    st.download_button(label="Download data as csv",data=csv_data,file_name="IMDB movies.csv",mime="text/csv")
