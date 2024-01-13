
import streamlit as st
import plotly.express as px
import geopandas as gpd
import numpy as np
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import matplotlib
import folium 
from streamlit_folium import folium_static

# List of empires
empires = [
    "Upper Egypt",
    "Old Kingdom of Egypt",
    "Akkadian Empire",
    "Indus Valley Civilisation",
    "Middle Kingdom of Egypt",
    "Xia dynasty",
    "Hyksos",
    "New Kingdom of Egypt",
    "Shang dynasty",
    "New Kingdom of Egypt",
    "Zhou dynasty",
    "Neo-Assyrian Empire",
    "Median Empire",
    "Achaemenid Empire",
    "Macedonian Empire",
    "Seleucid Empire",
    "Maurya Empire",
    "Han dynasty",
    "Xiongnu Empire",
    "Han dynasty"
]

# Read GeoJSON file
geojson_path = 'ancient_empires.geojson'

gdf = gpd.read_file(geojson_path) #create dataframe 


# Create a Streamlit app with a dropdown bar
st.title("Select An Empire")
selected_empire = st.selectbox("Select an Empire", gdf['Empire'].tolist())

# Display the selected empire
st.write(f"You selected: {selected_empire}")




#Display an empty map
st.title("World Map")
m=folium.Map(location= [0,0], zoom_start=5)
folium_static(m)





