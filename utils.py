# load the libraries
import streamlit as st
import requests,csv
import pandas as pd

class api_extracter:

    def __init__(self):
        self.api_key = st.secrets["API_KEY"]
        self.api_key2 = st.secrets["API_KEY2"]
        self.api_key3 = st.secrets["API_KEY3"]

    def get_data(self):
        url = "https://imdb232.p.rapidapi.com/api/title/get-most-popular"

        querystring = {"limit":"20","topMeterTitlesType":"ALL"}

        headers = {
            "x-rapidapi-key": self.api_key,
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

    def get_coming_soon(self):
        url = "https://imdb232.p.rapidapi.com/api/title/get-top-trending-video-trailers"

        querystring = {"limit":"20"}

        headers = {
            "x-rapidapi-key": self.api_key2,
            "x-rapidapi-host": "imdb232.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        xdata = data.get('data',{}).get('topTrendingTitles',{}).get('edges',{})

        urls= []
        titles = []
        for x in xdata:
            title = x.get('node',{}).get('item').get('latestTrailer',{}).get('primaryTitle',{}).get('titleText',{}).get('text',{})
            titles.append(title)
            y = x.get('node',{}).get('item',{}).get('latestTrailer',{}).get('playbackURLs',{})
            urls.append(y[1].get('url'))
        return titles,urls

    def get_top_actors(self):
        url = "https://imdb232.p.rapidapi.com/api/actors/get-most-popular"

        querystring = {"limit":"25"}

        headers = {
            "x-rapidapi-key": self.api_key3,
            "x-rapidapi-host": "imdb232.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        xdata = data.get('data',{}).get('topMeterNames',{}).get('edges',{})
        names = []
        ranks = []
        for x in xdata:
            title = x.get('node').get('nameText').get('text')
            rank = x.get('node').get('meterRanking').get('currentRank')
            names.append(title)
            ranks.append(rank)
        return names,ranks