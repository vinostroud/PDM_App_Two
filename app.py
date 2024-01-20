
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

#add function to pull geojson data based on select box.

def plot_geojson():
    selected_gdf = gdf[gdf['Empire'] == selected_empire]
    center_lat, center_lon = selected_gdf.geometry.centroid.y.mean(), selected_gdf.geometry.centroid.x.mean()
    m.location = [center_lat, center_lon]
    folium.GeoJson(selected_gdf, name=selected_empire, tooltip=selected_empire).add_to(m)

plot_geojson()
    
#tooltip = 'This is a placeholder tooltip'



folium_static(m)



