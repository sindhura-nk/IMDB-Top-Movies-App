# load the libraries
import streamlit as st
import requests,csv
import pandas as pd

class api_extracter:

    def __init__(self,api_key):
        self.api_key = st.secrets["API_KEY"]

    def get_data(self):
        url = "https://imdb232.p.rapidapi.com/api/title/get-most-popular"

        querystring = {"limit":"20","topMeterTitlesType":"ALL"}

        headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "imdb232.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        #print(response.json())
        data = response.json()

        nodes = data.get("data").get("topMeterTitles").get("edges")
        top_movie_data = []
        for node in nodes:
            nd = node.get("node",{})
            title = nd.get("titleText",{}).get("text",{})
            release_year = nd.get("releaseYear",{}).get("year",{})
            rank = nd.get("meterRanking",{}).get("currentRank",{})
            #print(title,release_year,rank)
            top_movie_data.append([title,release_year,rank])
        return top_movie_data

    def save_files_csv(self,data):
        with open("Top_movies_2.csv","w",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Movie Titles","Release Year","Rank"])
            writer.writerows(data)
        print("File is saved succesfully")