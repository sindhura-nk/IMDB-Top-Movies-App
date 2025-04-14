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

st.text("Welcome to this page. If you want to know latest information about movies and actors, you are at the right space. ")


# create a dropdown to display different options
options_info = ["20 Most Popular Movies","Top 25 Actors","20 Latest Video Trailers"]
option = st.selectbox("What would you like to know ?",options=options_info,index=None,placeholder="Select your input")

# After clicking the button, list of movies should get displayed
if option == "20 Most Popular Movies":
    data = client.get_data()
    df = pd.DataFrame(data,columns=["Movie Name","Release Year","Rank"])
    st.dataframe(df)

    csv_data = df.to_csv(index=False).encode("utf-8")
    # DOwnload button for user
    st.download_button(label="Download data as csv",data=csv_data,file_name="IMDB movies.csv",mime="text/csv")

if option == "20 Latest Video Trailers":
    titles,urls = client.get_coming_soon()

    for title,url in zip(titles,urls):
        st.markdown(f" - [{title}]({url})",unsafe_allow_html=True)

if option == "Top 25 Actors":
    names,ranks = client.get_top_actors()
    df = pd.DataFrame([names,ranks]).T
    df.columns = ["Actor's Name","Current Rank"]
    st.dataframe(df)

