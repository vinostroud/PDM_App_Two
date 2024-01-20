
import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
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

# create GeoDataFrame
gdf = gpd.read_file(geojson_path)

# Create a Streamlit app with a dropdown bar
st.title("Select An Empire")
selected_empire = st.selectbox("Select an Empire", gdf['Empire'].tolist())

# Display an empty map
st.title("World Map")
m = folium.Map(location=[0, 0], zoom_start=5)

tooltip = 'This is a placeholder tooltip'


folium_static(m)



